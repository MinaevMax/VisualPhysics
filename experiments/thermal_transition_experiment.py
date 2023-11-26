from vpython import *
from multiprocessing import Process

class ThermalTransitionExperiment(Process):

    def __init__(self, value):
        super(ThermalTransitionExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        m1 = box(pos=vector(0, 0, 0), length=10, height=0.5, width=25, color=color.blue)
        m2 = box(pos=vector(0, 4.5, 0), length=10, height=0.5, width=25, color=color.blue)
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            rate(100)

            if not self.is_run:
                break

            while m1.pos.y + m1.height < m2.pos.y:
                rate(200)

                if not self.is_run:
                    break

                m2.pos.y -= 0.05
            
            if not self.is_run:
                break

            for i in range(3):
                if not self.is_run:
                    break

                while m2.pos.z < 5:
                    rate(200)

                    if not self.is_run:
                        break

                    m2.pos.z += 0.03
                    m1.color.z -= 0.001
                    m1.color.x += 0.001
                    m2.color.z -= 0.001
                    m2.color.x += 0.001

                if not self.is_run:
                    break

                while m2.pos.z > -5:
                    rate(200)

                    if not self.is_run:
                        break

                    m2.pos.z -= 0.03
                    m1.color.z -= 0.001
                    m1.color.x += 0.001
                    m2.color.z -= 0.001
                    m2.color.x += 0.001
                
                if not self.is_run:
                    break

                while m2.pos.z < 0:
                    rate(200)

                    if not self.is_run:
                        break

                    m2.pos.z += 0.03
                    m1.color.z -= 0.001
                    m1.color.x += 0.001
                    m2.color.z -= 0.001
                    m2.color.x += 0.001
                
                if not self.is_run:
                    break
            
            if not self.is_run:
                break

            while m2.pos.y < 4.5:
                rate(200)

                if not self.is_run:
                    break

                m2.pos.y += 0.03

            if not self.is_run:
                break

            while m2.color.x >= 0:
                rate(200)

                if not self.is_run:
                    break

                m1.color.z += 0.001
                m1.color.x -= 0.001
                m2.color.z += 0.001
                m2.color.x -= 0.001
