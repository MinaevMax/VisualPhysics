from vpython import *
from multiprocessing import Process

class DiffractionExperiment(Process):

    def __init__(self, value):
        super(DiffractionExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        my1 = box(pos=vector(0, 10, 0), opacity=0.3, length=18, height=0.1, width=41, color=color.cyan)
        my2 = box(pos=vector(-20, 10, 0), opacity=0.3, length=18, height=0.1, width=41, color=color.cyan)
        my3 = box(pos=vector(20, 10, 0), opacity=0.3, length=18, height=0.1, width=41, color=color.cyan)
        my4 = box(pos=vector(0, -10, 0), opacity=0.3, length=60, height=0.1, width=41, color=color.cyan)
        my5 = box(pos=vector(14, 26, 0), opacity=0.3, length=26, height=0.1, width=41, color=color.cyan)
        my6 = box(pos=vector(-14, 26, 0), opacity=0.3, length=26, height=0.1, width=41, color=color.cyan)
        ri1 = []
        ri2 = []
        ri3 = []
        ch = 0
        ch1 = 0
        n1 = 0
        n = 0
        doch = 0
        ri1.append(ring(pos=vector(10, 10, 0),
        axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red, visible=False))
        ri2.append(ring(pos=vector(-10, 10, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red, visible=False))
        ri3.append(ring(pos=vector(0, 26, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red, visible=True))
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while len(ri3) <= 4:
            rate(400)

            if not self.is_run:
                break

            for i in range(len(ri3)):
                if not self.is_run:
                    break
                ri3[i].radius += 0.008
                ri3[i].pos.y -= 0.008

            if not self.is_run:
                break

            ch1 += 0.01

            if ch1 > 5:
                ch1 = 0
                ri3.append(ring(pos=vector(0, 26, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red))

        while True:
            if not self.is_run:
                break

            ri1[0].visible = True
            ri2[0].visible = True

            while True:
                rate(400)

                if not self.is_run:
                    break

                for i in range(len(ri3)):
                    if not self.is_run:
                        break

                    if i < len(ri1):
                        ri1[i].radius += 0.008
                        ri2[i].radius += 0.008
                        ri1[i].pos.y -= 0.008
                        ri2[i].pos.y -= 0.008

                    ri3[i].radius += 0.008
                    ri3[i].pos.y -= 0.008

                if not self.is_run:
                    break

                ch += 0.01

                if ch > 5 and len(ri1) <= 4:
                    ch = 0
                    ri1.append(ring(pos=vector(10, 10, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red))
                    ri2.append(ring(pos=vector(-10, 10, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red))

                if ch > 5 and len(ri1) > 4:
                    ch = 0
                    ri1[n].radius = 0.5
                    ri2[n].radius = 0.5
                    ri1[n].pos.y = 10
                    ri2[n].pos.y = 10
                    if n + 1 < len(ri1):
                        n += 1
                    else:
                        n = 0

                if ri3[n1].pos.y <= 10:
                    ri3[n1].radius = 0.5
                    ri3[n1].pos.y = 26
                    if n1 + 1 < len(ri3):
                        n1 += 1
                    else:
                        n1 = 0
