from vpython import *
from multiprocessing import Process

class RealLightSourceExperiment(Process):

    def __init__(self, value):
        super(RealLightSourceExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        m2 = box(pos=vector(10, 0, 0), length=2, height=25, width=3, color=color.cyan)
        ball_1_1 = sphere(pos=vector(-15, -3, 0), radius=0.3, color=color.red, make_trail=True)
        ball_1_3 = sphere(pos=vector(-15, 3, 0), radius=0.3, color=color.blue, make_trail=True)
        ball_1_2 = sphere(pos=vector(-15, 0, 0), radius=3, color=color.yellow)
        m1 = box(pos=vector(0, 0, 0), length=1.5, height=8, width=3, color=color.cyan)
        run = False
        xb1 = 0.05
        yb1 = -0.019
        xb2 = 0.05
        yb2 = 0.019
        flg = 0
        flag = 0
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            rate(1000)

            if not self.is_run:
                break

            yb1 += 0.0008
            yb2 -= 0.0008
            while yb1 <= 0.031:

                if not self.is_run:
                    break

                while flag == 0:
                    rate(500)

                    if not self.is_run:
                        break

                    if 0 <= ball_1_1.pos.x <= 0.5 and -4.2 <= ball_1_1.pos.y <= 4.2 or 10 <= ball_1_1.pos.x <= 10.5 and -40 <= ball_1_1.pos.y <= 40:
                        flag = 1
                    elif 0 <= ball_1_3.pos.x <= 0.5 and -4.2 <= ball_1_3.pos.y <= 4.2 or 10 <= ball_1_3.pos.x <= 10.5 and -40 <= ball_1_3.pos.y <= 40:
                        flag = 3
                    ball_1_1.pos.x += xb1
                    ball_1_1.pos.y += yb1
                    ball_1_3.pos.x += xb2
                    ball_1_3.pos.y += yb2

                if not self.is_run:
                    break

                if flag == 1:
                    yb1 += 0.0008
                    ball_1_1.make_trail = False
                    ball_1_1.pos.x = -15
                    ball_1_1.pos.y = -3
                    ball_1_1.make_trail = True
                elif flag == 3:
                    yb2 -= 0.0008
                    ball_1_3.make_trail = False
                    ball_1_3.pos.x = -15
                    ball_1_3.pos.y = 3
                    ball_1_3.make_trail = True
                flag = 0

            if not self.is_run:
                break