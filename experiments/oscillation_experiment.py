from vpython import *
from multiprocessing import Process

class OscillationExperiment(Process):

    def __init__(self, value):
        super(OscillationExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        self.pendulums = []

        hinge = cylinder(pos = vec(0, 10, -15), axis = vec(0, 0, 1), size = vec(30, .8, .8), color = vec(.5, .5, .8))
        
        for i in range(15):
            p = sphere(radius = 0.8, color = color.hsv_to_rgb(vec(i / 20, 0.6, 0.8)))
            p.theta0 = -0.6
            p.period = 60 / (51 + i)
            p.wire = cylinder()
            p.wire.color = p.color
            p.wire.pos = hinge.pos + vec(0, 0, i + .5) * hinge.size.x / 15
            p.wire.size = vec(15 * p.period * p.period, .1, .1)
            self.pendulums.append(p)

        self.t = 0
        self.dt = 0.001
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            rate(1000)

            for p in self.pendulums:
                if not self.is_run:
                    break
                
                theta = p.theta0 * cos(2 * pi * self.t / p.period)
                p.wire.axis = p.wire.size.x * vec(sin(theta), -cos(theta), 0)
                p.pos = p.wire.pos + p.wire.axis

            if not self.is_run:
                break
            
            self.t = self.t + self.dt
