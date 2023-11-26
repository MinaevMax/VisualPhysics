from vpython import *
from multiprocessing import Process

class ConvectionExperiment(Process):

    def __init__(self, value):
        super(ConvectionExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        c = curve()
        c.append(pos=vector(-11, -11, 0), color=color.red, radius=0.5)
        c.append(pos=vector(-11, 11, 0), color=color.red, radius=0.5)
        c.append(pos=vector(11, 11, 0), color=color.yellow, radius=0.5)
        c.append(pos=vector(11, -11, 0), color=color.blue, radius=0.5)
        c.append(pos=vector(-11, -11, 0), color=color.red, radius=0.5)
        ball_1 = sphere(pos=vector(10, 10, 0), radius=0.5, color=color.yellow)
        ball_2 = sphere(pos=vector(-10, 10, 0), radius=0.5, color=color.red)
        ball_3 = sphere(pos=vector(-10, -10, 0), radius=0.5, color=color.red)
        ball_4 = sphere(pos=vector(10, -10, 0), radius=0.5, color=color.blue)
        mybox1 = box(pos=vector(-12, 0, 0), length=2, height=26, width=1, opacity=0.3, color=color.blue)
        mybox2 = box(pos=vector(12, 0, 0), length=2, height=26, width=1, opacity=0.3, color=color.blue)
        mybox3 = box(pos=vector(0, 12, 0), length=22, height=2, width=1, opacity=0.3, color=color.blue)
        mybox4 = box(pos=vector(0, -12, 0), length=22, height=2, width=1, opacity=0.3, color=color.blue)
        mybox5 = box(pos=vector(-12, -12, 0), length=2, height=2, width=2, color=color.red)
        T1 = text(text='Холодная среда', pos=vector(-5, 11.5, 0.5), height=1, color=color.black)
        T2 = text(text='Холодная среда', pos=vector(-5, -12.5, 0.5), height=1, color=color.black)
        T3 = text(text='Холодная среда', pos=vector(-11.5, -5, 0.5), axis=vector(0, 1, 0), height=1, color=color.black)
        T4 = text(text='Холодная среда', pos=vector(11.5, 5, 0.5), axis=vector(0, -1, 0), height=1, color=color.black)
        T5 = text(text='Нагреватель', pos=vector(-15, -14, 0.5), height=0.8, color=color.red)
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            rate(500)

            if not self.is_run:
                break

            if ball_1.pos.x >= 10 and ball_1.pos.y >= 10:
                pos = 1
            if ball_1.pos.x >= 10 and ball_1.pos.y <= -10:
                pos = 2
            if ball_1.pos.x <= -10 and ball_1.pos.y <= -10:
                pos = 3
            if ball_1.pos.x <= -10 and ball_1.pos.y >= 10:
                pos = 4
            if pos == 1:
                ball_3.color = color.red

                ball_2.color.y += 0.0005

                ball_1.color.y -= 0.0005
                ball_1.color.x -= 0.0005
                ball_1.color.z += 0.0005

                ball_4.color.x += 0.0005
                ball_4.color.z -= 0.0005

                ball_1.pos.y -= 0.01
                ball_2.pos.x += 0.01
                ball_3.pos.y += 0.01
                ball_4.pos.x -= 0.01
            if pos == 2:
                ball_4.color = color.red

                ball_3.color.y += 0.0005
                
                ball_2.color.y -= 0.0005
                ball_2.color.x -= 0.0005
                ball_2.color.z += 0.0005
                
                ball_1.color.x += 0.0005
                ball_1.color.z -= 0.0005

                ball_1.pos.x -= 0.01
                ball_2.pos.y -= 0.01
                ball_3.pos.x += 0.01
                ball_4.pos.y += 0.01
            if pos == 3:
                ball_1.color = color.red
                
                ball_4.color.y += 0.0005
                
                ball_3.color.y -= 0.0005
                ball_3.color.x -= 0.0005
                ball_3.color.z += 0.0005

                ball_2.color.x += 0.0005
                ball_2.color.z -= 0.0005

                
                ball_1.pos.y += 0.01
                ball_2.pos.x -= 0.01
                ball_3.pos.y -= 0.01
                ball_4.pos.x += 0.01
            if pos == 4:
                ball_2.color = color.red
                
                ball_1.color.y += 0.0005
                
                ball_4.color.y -= 0.0005
                ball_4.color.x -= 0.0005
                ball_4.color.z += 0.0005
                
                ball_3.color.x += 0.0005
                ball_3.color.z -= 0.0005

                ball_1.pos.x += 0.01
                ball_2.pos.y += 0.01
                ball_3.pos.x -= 0.01
                ball_4.pos.y -= 0.01
