from vpython import *
from multiprocessing import Process

class GravitationExperiment(Process):

    def __init__(self, value):
        super(GravitationExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        ball_1_1 = sphere(pos=vector(0, 10, 0), radius=0.5, color=color.red)
        mybox1 = box(pos=vector(0, -9.6, 0), length=10, height=1, width=10, texture=textures.metal)
        invisible_box = box(pos=vector(0, -10, 0), length=1, height=1, width=1, visible=False)
        u = 0
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            if not self.is_run:
                break

            for i in range(200):
                rate(1000)
                if not self.is_run:
                    break
                invisible_box.pos.x += 0.0001

            if not self.is_run:
                break
            
            while ball_1_1.pos.y >= -8:
                if not self.is_run:
                    break

                for i in range(200):
                    rate(5000)
                    if not self.is_run:
                        break
                    invisible_box.pos.x += 0.0001
                
                if not self.is_run:
                    break

                u += 0.1
                ball_1_1.pos.y -= u
            
            if not self.is_run:
                break
            
            for i in range(200):
                rate(100)
                if not self.is_run:
                    break
                invisible_box.pos.x += 0.0001
            
            if not self.is_run:
                break

            ball_1_1.pos.y = 10
            u = 0
