from vpython import *
from multiprocessing import Process

class ThermalRadiationExperiment(Process):

    def __init__(self, value):
        super(ThermalRadiationExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        ball_1_1 = sphere(pos=vector(0, 0, 0), radius=0.5, opacity=0.4, color=color.red)
        ball_1_2 = sphere(pos=vector(-1, 0, 0), radius=0.2, color=color.blue)
        ball_1_3 = sphere(pos=vector(1, 0, 0), radius=0.2, color=color.blue)
        ri1 = []
        ch = 0
        n = 0
        ri1.append(ring(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.01, color=color.red, visible=True))
        # ball_1_1 = sphere(pos=vector(0, 0, 0), radius=0.5, opacity=0.4, color=color.red)
        # ball_1_2 = sphere(pos=vector(-1, 0, 0), radius=0.2, color=color.blue)
        # ball_1_3 = sphere(pos=vector(1, 0, 0), radius=0.2, color=color.blue)
        # run = False
        # ri1 = []
        # ch = 0
        # n = 0
        # ri1.append(ring(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.01, color=color.red, visible=True))
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while len(ri1) <= 2:
            rate(50)

            if not self.is_run:
                break

            for i in range(len(ri1)):
                if not self.is_run:
                    break

                ri1[i].radius += 0.008
            
            if not self.is_run:
                break

            ch += 0.01
            if ch > 0.5:
                ch = 0
                ri1.append(ring(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.01, color=color.red))

        while ball_1_2.color.z > 0:
            rate(50)

            if not self.is_run:
                break

            for i in range(len(ri1)):
                if not self.is_run:
                    break
                
                ri1[i].radius += 0.008

            if not self.is_run:
                break
                
            ball_1_2.color.x += 0.005
            ball_1_2.color.z -= 0.005
            ball_1_3.color.x += 0.005
            ball_1_3.color.z -= 0.005
            ch += 0.01
            if ch > 0.5:
                ch = 0
                ri1[n].radius = 0.5
                if n + 1 < len(ri1):
                    n += 1
                else:
                    n = 0
