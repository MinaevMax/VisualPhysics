from vpython import *
from multiprocessing import Process

class InelasticCollisionExperiment(Process):

    def __init__(self, value):
        super(InelasticCollisionExperiment, self).__init__()

        self.value = value

    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()
        
        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        rod1 = cylinder(pos=vector(0, 1.5, 0), axis=vector(2, 0, 0), radius=1, texture=textures.metal)
        rod2 = cylinder(pos=vector(0, 1.5, -10), axis=vector(2, 0, 0), radius=1, texture=textures.metal)
        my = box(pos=vector(0, 0, 0), length=10, height=1, width=25, texture=textures.rock)
        b1 = vector(0, 1.5, 0)
        b2 = vector(0, 1.5, -10)

        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))
        
        while True:
            rate(1000)

            while b2.z + 2 < b1.z:
                rate(200)
                if not self.is_run:
                    break
                rod2.rotate(angle=0.02, axis=vector(1, 0, 0), origin=rod2.pos)
                rod2.pos = b2
                b2.z += 0.016

            while b1.z < 10:
                rate(200)
                if not self.is_run:
                    break
                rod1.rotate(angle=0.01, axis=vector(1, 0, 0), origin=rod1.pos)
                rod2.rotate(angle=0.01, axis=vector(1, 0, 0), origin=rod2.pos)
                rod2.pos = b2
                b2.z += 0.008
                rod1.pos = b1
                b1.z += 0.008
            
            if not self.is_run:
                break
            
            b1.z = 0
            b2.z = -10
            rod1.pos = b1
            rod2.pos = b2
