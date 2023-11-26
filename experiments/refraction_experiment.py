from vpython import *
from multiprocessing import Process

class RefractionExperiment(Process):

    def __init__(self, value):
        super(RefractionExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        ball_1_1 = sphere(pos=vector(0, 8, -8), radius=0.3, color=color.red, make_trail=True, retain=100)
        my = box(pos=vector(0, 0, -2), opacity=0.3, length=-8, height=5, width=20, color=color.cyan)
        b = vector(0, 8, -8)
        pl1 = -0.008
        pl2 = 0.008
        td = 1
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            rate(200)

            if not self.is_run:
                break

            ball_1_1.pos = b
            b.z += pl2
            b.y += pl1

            if ball_1_1.pos.y + 0.3 < my.pos.y + 3 and td == 1:
                pl2 = 0.002

            if ball_1_1.pos.y < my.pos.y - 2.5 and td == 1:
                pl2 = 0.008

            if ball_1_1.pos.y < -8 and td == 1:
                pl2 = -0.008
                pl1 = 0.008
                td = 2

            if ball_1_1.pos.y > my.pos.y - 2.5 and td == 2:
                pl2 = -0.002

            if ball_1_1.pos.y + 0.3 > my.pos.y + 3 and td == 2:
                pl2 = -0.008
                pl1 = 0.008

            if ball_1_1.pos.y > 8 and td == 2:
                pl1 = -0.008
                pl2 = 0.008
                td = 1
