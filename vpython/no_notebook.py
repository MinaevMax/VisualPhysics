import asyncio
import copy
import json
import os
import platform
import signal
import socket
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote

import txaio
from autobahn.asyncio.websocket import WebSocketServerProtocol, WebSocketServerFactory

from .rate_control import rate
from .vpython import GlowWidget, baseObj, vector


# Check for Ctrl+C. SIGINT will also be sent by our code if WServer is closed.
def signal_handler(signal, frame):
    stop_server()


signal.signal(signal.SIGINT, signal_handler)


def find_free_port():
    s = socket.socket()
    s.bind(('', 0))
    return s.getsockname()[1]


__HTTP_PORT = 63794
__SOCKET_PORT = find_free_port()

# Make it possible for glowcomm.html to find out what the websocket port is:
js = __file__.replace(
    'no_notebook.py', 'vpython_libraries' + os.sep + 'glowcomm.html')

with open(js) as fd:
    glowcomm_raw = fd.read()


def glowcomm_with_socket_port(port):
    global glowcomm_raw
    # provide glowcomm.html with socket number
    return glowcomm_raw.replace('XXX', str(port))


glowcomm = glowcomm_with_socket_port(__SOCKET_PORT)

httpserving = False
websocketserving = False


class serveHTTP(BaseHTTPRequestHandler):
    serverlib = __file__.replace('no_notebook.py', 'vpython_libraries')
    serverdata = __file__.replace('no_notebook.py', 'vpython_data')
    mimes = {'html': ['text/html', serverlib],
             'js': ['application/javascript', serverlib],
             'css': ['text/css', serverlib],
             'jpg': ['image/jpg', serverdata],
             'png': ['image/png', serverlib],
             'otf': ['application/x-font-otf', serverdata],
             'ttf': ['application/x-font-ttf', serverdata],
             'ico': ['image/x-icon', serverdata]}

    def do_GET(self):
        global httpserving
        httpserving = True
        html = False
        if self.path == "/":
            self.path = 'glowcomm.html'
            html = True
        elif self.path[0] == "/":
            self.path = os.sep + self.path[1:]
        f = self.path.rfind('.')
        fext = None
        if f > 0:
            fext = self.path[f + 1:]
        if fext in self.mimes:
            mime = self.mimes[fext]
            # For example, mime[0] is image/jpg,
            # mime[1] is C:\Users\Bruce\Anaconda3\lib\site-packages\vpython\vpython_data
            self.send_response(200)
            self.send_header('Content-type', mime[0])
            self.end_headers()
            if not html:
                path = unquote(self.path)  # convert %20 to space, for example
                # Now a path can be for example \Fig 4.6.jpg
                # user current working directory, e.g. D:\Documents\0GlowScriptWork\LocalServer
                cwd = os.getcwd()
                loc = cwd + path
                if not os.path.isfile(loc):
                    loc = mime[1] + path  # look in vpython_data
                fd = open(loc, 'rb')
                self.wfile.write(fd.read())
            else:
                # string.encode() is not available in Python 2.7, but neither is async
                self.wfile.write(glowcomm.encode('utf-8'))

    def log_message(self, format, *args):  # this override server stderr output
        return


# Requests from client to websocket server can be the following:
# trigger event; return data (constructors, attributes, methods)
# another event; pause, waitfor, pick, compound


class WSserver(WebSocketServerProtocol):
    # Data sent and received must be type "bytes", so use string.encode and string.decode
    connection = None

    def onConnect(self, request):
        self.connection = self

    def onOpen(self):
        global websocketserving
        websocketserving = True

    # For Python 3.5 and later, the newer syntax eliminates "@asyncio.coroutine"
    # in favour of "async def onMessage...", and "yield from" with "await".
    # Attempting to use the older Python 3.4 syntax was not successful, so this
    # no-notebook version of VPython requires Python 3.5.3 or later.
    # @asyncio.coroutine
    # def onMessage(self, data, isBinary): # data includes canvas update, events, pick, compound
    # data includes canvas update, events, pick, compound
    async def onMessage(self, data, isBinary):
        baseObj.handle_attach()  # attach arrow and attach trail

        baseObj.sent = False  # tell the main thread that we're preparing to send data to the browser
        while True:
            try:
                objdata = copy.deepcopy(baseObj.updates)
                attrdata = copy.deepcopy(baseObj.attrs)
                baseObj.initialize()  # reinitialize baseObj.updates
                break
            except:
                pass
        for a in attrdata:  # a is [idx, attr]
            idx, attr = a
            val = getattr(baseObj.object_registry[idx], attr)
            if type(val) is vector:
                val = [val.x, val.y, val.z]
            if idx in objdata['attrs']:
                objdata['attrs'][idx][attr] = val
            else:
                objdata['attrs'][idx] = {attr: val}
        objdata = baseObj.package(objdata)
        jdata = json.dumps(objdata, separators=(',', ':')).encode('utf_8')
        self.sendMessage(jdata, isBinary=False)
        baseObj.sent = True

        if data != b'trigger':  # b'trigger' just asks for updates
            d = json.loads(data.decode("utf_8"))  # update_canvas info
            for m in d:
                # Must send events one at a time to GW.handle_msg because bound events need the loop code:
                # message format used by notebook
                msg = {'content': {'data': [m]}}
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, GW.handle_msg, msg)

    def onClose(self, wasClean, code, reason):
        """Called when browser tab is closed."""
        global websocketserving

        self.connection = None

        # We're done serving, let everyone else know...
        websocketserving = False

        # We want to exit, but the main thread is running.
        # Only the main thread can properly call sys.exit, so have a signal
        # handler call it on the main thread's behalf.
        if platform.system() == 'Windows':
            if threading.main_thread().is_alive():
                # On windows, if we get here then this signal won't be caught
                # by our signal handler. Call it ourselves.
                os.kill(os.getpid(), signal.CTRL_C_EVENT)
            else:
                stop_server()
        else:
            os.kill(os.getpid(), signal.SIGINT)


try:
    __server = HTTPServer(('', __HTTP_PORT), serveHTTP)
except:
    pass

__w = threading.Thread(target=__server.serve_forever)
__w.start()


def start_websocket_server():
    """
    Function to get the websocket server going and run the event loop
    that feeds it.
    """
    # We need a new loop in case some other process has already started the
    # main loop. In principle, we might be able to do a check for a running
    # loop, but this works whether a loop is running.
    __interact_loop = asyncio.new_event_loop()

    # Need to do two things before starting the server factory:
    #
    # 1. Set our loop to be the default event loop on this thread
    asyncio.set_event_loop(__interact_loop)
    # 2. The line below is courtesy of
    # https://github.com/crossbario/autobahn-python/issues/1007#issuecomment-391541322
    txaio.config.loop = __interact_loop

    # Now create the factory, start the server, then run the event loop forever.
    __factory = WebSocketServerFactory(u"ws://localhost:{}/".format(__SOCKET_PORT))
    __factory.protocol = WSserver
    __coro = __interact_loop.create_server(__factory, '0.0.0.0', __SOCKET_PORT)
    __interact_loop.run_until_complete(__coro)
    __interact_loop.run_forever()


# Put the websocket server in a separate thread running its own event loop.
# That works even if some other program (e.g. spyder) already running an
# async event loop.
__t = threading.Thread(target=start_websocket_server)
__t.start()


def stop_server():
    """Shuts down all threads and exits cleanly."""
    global __server
    __server.shutdown()
    event_loop = txaio.config.loop
    event_loop.stop()
    # We've told the event loop to stop, but it won't shut down until we poke
    # it with a simple scheduled task.
    event_loop.call_soon_threadsafe(lambda: None)

    if threading.main_thread().is_alive():
        sys.exit(0)
    else:
        pass
        # If the main thread has already stopped, the python interpreter
        # is likely just running .join on the two remaining threads (in
        # python/threading.py:_shutdown). Since we just stopped those threads,
        # we'll now exit.


GW = GlowWidget()

while not (httpserving and websocketserving):  # try to make sure the setup is complete
    rate(60)

_ = None
