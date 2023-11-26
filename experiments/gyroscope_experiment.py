from vpython import *
from multiprocessing import Process

class GyroscopeExperiment(Process):

    def __init__(self, value):
        super(GyroscopeExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0
    
    def reset(self):
        self.theta = 0.3*pi
        self.thetadot = 0
        self.psi = 0
        self.psidot = 30
        self.phi = -pi/2
        self.phidot = 0
        if self.pureprecession:
            a = (1-self.I3/self.I1)*sin(self.theta)*cos(self.theta)
            b = -(self.I3/self.I1)*self.psidot*sin(self.theta)
            c = self.M*self.g*self.r*sin(self.theta)/self.I1
            self.phidot = (-b+sqrt(b**2-4*a*c))/(2*a)
        self.gyro.axis = self.gyro.length*vector(sin(self.theta)*sin(self.phi),cos(self.theta),sin(self.theta)*cos(self.phi))
        A = norm(self.gyro.axis)
        self.gyro.pos = 0.5*self.Lshaft*A
        self.tip.pos = self.Lshaft*A
        self.tip.clear_trail()

    def run(self):
        self.canvas = canvas(width=965, height=600, range=1.2, background=color.white)

        self.Lshaft = 1
        self.r = self.Lshaft/2
        Rshaft = 0.03
        self.M = 1
        Rrotor = 0.4
        Drotor = 0.1
        self.I3 = 0.5*self.M*Rrotor**2
        self.I1 = self.M*self.r**2 + .5*self.I3
        hpedestal = self.Lshaft
        wpedestal = 0.1
        tbase = 0.05
        wbase = 3*wpedestal
        self.g = 9.8
        Fgrav = vector(0,-self.M*self.g,0)
        top = vector(0,0,0)

        shaft = cylinder(length=self.Lshaft, radius=Rshaft, color=color.orange)
        rotor = cylinder(pos=vector(self.Lshaft/2-Drotor/2,0,0), axis=vector(Drotor, 0, 0), radius=Rrotor, color=color.gray(0.9))
        base = sphere(color=shaft.color, radius=Rshaft)
        end = sphere(pos=vector(self.Lshaft,0,0), color=shaft.color, radius=Rshaft)
        self.gyro = compound([shaft, rotor, base, end])
        gyro_center = self.gyro.pos
        self.gyro.texture = textures.metal
        self.tip = sphere(pos=shaft.axis, radius=shaft.radius/2,  make_trail=True, retain=250)
        self.tip.trail_color = color.green
        self.tip.trail_radius = 0.15*Rshaft

        pedestal = box(pos=top-vector(0,hpedestal/2+shaft.radius/2,0), height=hpedestal-shaft.radius, length=wpedestal, width=wpedestal, texture=textures.wood)
        pedestal_base = box(pos=top-vector(0,hpedestal+tbase/2,0), height=tbase, length=wbase, width=wbase, texture=textures.wood)

        self.theta = 0
        self.thetadot = 0
        self.psi = 0
        self.psidot = 0
        self.phi = 0
        self.phidot = 0
        self.pureprecession = False

        self.reset()
        scene.waitfor('textures')

        dt = 0.0001
        t = 0
        Nsteps = 20
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            rate(200)

            if not self.is_run:
                break

            for step in range(Nsteps):
                if not self.is_run:
                    break

                atheta = sin(self.theta)*cos(self.theta)*self.phidot**2+( self.M*self.g*self.r*sin(self.theta)-self.I3*(self.psidot+self.phidot*cos(self.theta))*self.phidot*sin(self.theta))/self.I1
                aphi = (self.I3/self.I1)*(self.psidot+self.phidot*cos(self.theta))*self.thetadot/sin(self.theta)-2*cos(self.theta)*self.thetadot*self.phidot/sin(self.theta)
                apsi = self.phidot*self.thetadot*sin(self.theta)-aphi*cos(self.theta)

                self.thetadot += atheta*dt
                self.phidot += aphi*dt
                self.psidot += apsi*dt

                self.theta += self.thetadot*dt
                self.phi += self.phidot*dt
                self.psi += self.psidot*dt

            if not self.is_run:
                break

            self.gyro.axis = self.gyro.length*vector(sin(self.theta)*sin(self.phi),cos(self.theta),sin(self.theta)*cos(self.phi))

            self.gyro.rotate(angle=self.psidot*dt*Nsteps)
            A = norm(self.gyro.axis)
            self.gyro.pos = 0.5*self.Lshaft*A
            self.tip.pos = self.Lshaft*A
            t = t+dt*Nsteps
