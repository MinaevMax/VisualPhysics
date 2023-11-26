from vpython import *
from multiprocessing import Process

class PointLightSourceExperiment(Process):

    def __init__(self, value):
        super(PointLightSourceExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, center=vector(5,0,0), background=color.white)

        m1 = box(pos=vector(0, 0, 0), length=1, height=8, width=3, color=color.cyan)
        m2 = box(pos=vector(10, 0, 0), length=2, height=25, width=3, color=color.cyan)
        ball_1_1 = sphere(pos=vector(-15, 0, 0), radius=0.3, color=color.red, make_trail=True)
        ball_1_2 = sphere(pos=vector(-15, 0, 0), radius=0.5, color=color.yellow)
        xb = 0
        yb = -0.025
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            rate(1000)

            if not self.is_run:
                break

            while yb <= 0.025:
                if not self.is_run:
                    break

                xb = 0.05
                yb += 0.001
                while not(0 <= ball_1_1.pos.x <= 0.01 and -4.2 <= ball_1_1.pos.y <= 4.2) and not(10 <= ball_1_1.pos.x <= 10.5 and -40 <= ball_1_1.pos.y <= 40):
                    rate(500)
                
                    if not self.is_run:
                        break
                
                    ball_1_1.pos.x += xb
                    ball_1_1.pos.y += yb

                if not self.is_run:
                    break

                ball_1_1.make_trail = False
                ball_1_1.pos.x = -15
                ball_1_1.pos.y = 0
                ball_1_1.make_trail = True
