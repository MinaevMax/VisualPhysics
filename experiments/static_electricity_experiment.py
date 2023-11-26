from vpython import *
from multiprocessing import Process

class StaticElectricityExperiment(Process):

    def __init__(self, value):
        super(StaticElectricityExperiment, self).__init__()

        self.value = value

    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        ball_1_1 = sphere(pos=vector(-2, 1, 1), radius=0.3, color=color.cyan)
        ball_1_2 = sphere(pos=vector(0, 1, -1), radius=0.3, color=color.cyan)
        ball_1_3 = sphere(pos=vector(2, 1, 1), radius=0.3, color=color.cyan)
        ball_2_1 = sphere(pos=vector(-2, 4, -1), radius=0.3, color=color.cyan)
        ball_2_2 = sphere(pos=vector(0, 4, 1), radius=0.3, color=color.cyan)
        ball_2_3 = sphere(pos=vector(2, 4, -1), radius=0.3, color=color.cyan)
        m1 = box(pos=vector(0, 0.5, 0), length=10, height=0.5, width=25, texture=textures.rug)
        m2 = box(pos=vector(0, 4.5, 0), length=10, height=0.5, width=25, texture=textures.rug)

        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            rate(1000)

            if not self.is_run:
                break

            while m1.pos.y + m1.height * 2 < m2.pos.y:
                rate(200)
                if not self.is_run:
                    break
                m2.pos.y -= 0.01
                ball_2_1.pos.y -= 0.01
                ball_2_2.pos.y -= 0.01
                ball_2_3.pos.y -= 0.01

            while m2.pos.z < 5:
                rate(200)
                if not self.is_run:
                    break
                m2.pos.z += 0.01
                ball_2_1.pos.z += 0.01
                ball_2_2.pos.z += 0.01
                ball_2_3.pos.z += 0.01

            while m2.pos.z > -5:
                rate(200)
                if not self.is_run:
                    break
                m2.pos.z -= 0.01
                ball_2_1.pos.z -= 0.01
                ball_2_2.pos.z -= 0.01
                ball_2_3.pos.z -= 0.01
                
            while m2.pos.z < 0:
                rate(200)
                if not self.is_run:
                    break
                m2.pos.z += 0.01
                ball_2_1.pos.z += 0.01
                ball_2_2.pos.z += 0.01
                ball_2_3.pos.z += 0.01

            while m2.pos.y < 4.5:
                rate(200)
                if not self.is_run:
                    break
                m2.pos.y += 0.01
                ball_2_1.pos.y += 0.01
                ball_1_1.pos.y += 0.01
                ball_2_3.pos.y += 0.01
                ball_2_2.pos.y += 0.01
                ball_1_3.pos.y += 0.01

            if not self.is_run:
                    break
            
            ball_1_1.pos.y = 1
            ball_1_3.pos.y = 1
