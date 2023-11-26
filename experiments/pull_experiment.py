from vpython import *
from multiprocessing import Process

class PullExperiment(Process):

    def __init__(self, value):
        super(PullExperiment, self).__init__()

        self.value = value

    def on_return_button_press(r, self):
        self.canvas.delete()
        self.return_button.delete()
        self.repeat_button.delete()

        self.is_run = False
        self.value.value = 0
        
    def on_repeat_button_press(r, self):
        self.alpha.pos = vector(-self.xstart, self.b, 0)
        self.target.pos = vector(0, self.b-0.00000000000004, 0)
        self.alpha.p = vector(sqrt(2. * self.alpha.mass * self.ke), 0, 0)
        self.target.mass = self.targetproperties[1]*self.mproton
        self.target.radius = (self.target.mass/self.mproton)**(1./3.)*self.rproton
        self.target.q = self.targetproperties[0]*self.qe
        self.target.p = vector(0,0,0)
        dt = (5.*self.xstart/(mag(self.alpha.p)/self.alpha.mass)/1e5)*10
        ptot = self.alpha.p+self.target.p
        vcm = ptot / (self.alpha.mass + self.target.mass)

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white, fov=0.01, range=200e-15, x=0, y=0)

        self.b = 15e-15

        projectileproperties = (2, 4)

        self.targetproperties = (8, 16)

        rpscale = 2
        parroVisible = 1

        range0 = 200e-15
        self.xstart = 0.95*range0

        kcoul = 9e9
        self.qe = 1.6e-19
        self.mproton = 1.7e-27
        self.rproton = 1.3e-15*rpscale
        self.alpha = sphere(pos=vector(-self.xstart, self.b, 0), color=color.red, make_trail=True, interval=40, retain=50)
        self.target = sphere(pos=vector(0, self.b-0.00000000000004, 0), color=color.blue, make_trail=True, interval=40, retain=50)
        self.alpha.mass = projectileproperties[1]*self.mproton
        self.alpha.radius = (self.alpha.mass/self.mproton)**(1./3.)*self.rproton
        self.alpha.q = projectileproperties[0]*self.qe
        self.ke = 1e6*self.qe
        self.alpha.p = vector(sqrt(2.*self.alpha.mass*self.ke),0,0)
        self.target.mass = self.targetproperties[1]*self.mproton
        self.target.radius = (self.target.mass/self.mproton)**(1./3.)*self.rproton
        self.target.q = self.targetproperties[0]*self.qe
        self.target.p = vector(0,0,0)
        dt = (5.*self.xstart/(mag(self.alpha.p)/self.alpha.mass)/1e5)*10
        ptot = self.alpha.p+self.target.p
        vcm = ptot/(self.alpha.mass+self.target.mass)

        pscale = 40e-15/4e-20
        paarro = arrow(pos=self.alpha.pos, axis=self.alpha.p*pscale, color=color.cyan, shaftwidth = 0.5*self.alpha.radius, fixedwidth=1, visible=parroVisible)
        ptarro = arrow(pos=self.target.pos, axis=self.target.p*pscale, color=color.magenta, shaftwidth = 0.5*self.alpha.radius, fixedwidth=1, visible=parroVisible)
        
        self.is_run = True

        self.return_button = button(text='Назад', bind=lambda: self.on_return_button_press(self))
        self.repeat_button = button(text='Повторить', bind=lambda: self.on_repeat_button_press(self))

        while True:
            rate(500)

            if not self.is_run:
                break

            r12 = self.alpha.pos-self.target.pos
            F = -(kcoul * self.alpha.q * self.target.q / mag(r12)**2) * norm(r12)
            self.alpha.p = self.alpha.p + F*dt
            self.target.p = self.target.p - F*dt
            self.alpha.pos = self.alpha.pos + (self.alpha.p/self.alpha.mass)*dt
            self.target.pos = self.target.pos + (self.target.p/self.target.mass)*dt
            paarro.pos = self.alpha.pos
            paarro.axis = self.alpha.p*pscale
            ptarro.pos = self.target.pos
            ptarro.axis = self.target.p*pscale
