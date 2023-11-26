from vpython import *
from multiprocessing import Process

class HeatExchangeExperiment(Process):

    def __init__(self, value):
        super(HeatExchangeExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        ball_1_1 = sphere(pos=vector(-1.5, 0, 0), radius=0.5, opacity=0.4, color=color.red)
        ball_1_2 = sphere(pos=vector(1.5, 0, 0), radius=0.5, opacity=0.4, color=color.blue)
        ri1 = []
        ch = 0
        n = 0
        ri2 = []
        ri1.append(ring(pos=vector(-1.5, 0, 0), axis=vector(1, 0, 0), radius=0.5, thickness=0.02, color=color.red, visible=True))
        ri2.append(ring(pos=vector(1.5, 0, 0), axis=vector(1, 0, 0), radius=0.5, thickness=0.02, color=color.blue, visible=True))
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while len(ri1) <= 2:
            rate(50)

            if not self.is_run:
                    break

            for i in range(len(ri1)):
                if not self.is_run:
                    break

                ri1[i].pos.x += 0.01
                ri2[i].pos.x -= 0.01

            if not self.is_run:
                break

            ch += 0.01
            if ch > 1:
                ch = 0
                ri1.append(ring(pos=vector(-1.5, 0, 0), axis=vector(1, 0, 0), radius=0.5, thickness=0.02, color=color.red))
                ri2.append(ring(pos=vector(1.5, 0, 0), axis=vector(1, 0, 0), radius=0.5, thickness=0.02, color=color.blue))

        while ball_1_1.color.x >= ball_1_2.color.x:
            rate(50)

            if not self.is_run:
                break

            for i in range(len(ri1)):
                if not self.is_run:
                    break

                ri1[i].pos.x += 0.01
                ri2[i].pos.x -= 0.01

            if not self.is_run:
                break

            ch += 0.01
            if ch > 1:
                ch = 0
                ri1[n].pos.x = -1.5
                ri1[n].color = ball_1_1.color
                ri2[n].pos.x = 1.5
                ri2[n].color = ball_1_2.color
                if n + 1 < len(ri1):
                    n += 1
                else:
                    n = 0
            ball_1_1.color.x -= 0.001
            ball_1_1.color.z += 0.001
            ball_1_2.color.x += 0.001
            ball_1_2.color.z -= 0.001

        if self.is_run:
            ri1[0].visible = False
            ri1[1].visible = False
            ri1[2].visible = False
            ri2[0].visible = False
            ri2[1].visible = False
            ri2[2].visible = False
