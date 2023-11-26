from vpython import *
from multiprocessing import Process

class ExpansionExperiment(Process):

    def __init__(self, value):
        super(ExpansionExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        ball_1_1 = sphere(pos=vector(0, 8, 0), radius=2, color=color.blue)
        mybox1 = box(pos=vector(-2.5, 0.5, 0), length=1, height=10, width=1, texture=textures.metal)
        mybox2 = box(pos=vector(-2.5, -4, 0), length=3, height=1, width=3, texture=textures.metal)
        ring(pos=vector(0, 5, 0), axis=vector(0, 1, 0), radius=2.05, thickness=0.1, texture=textures.metal)
        mybox5 = box(pos=vector(3, 8, 0), length=2, height=2, width=2, color=color.red, visible=False)
        invisible_box = box(pos=vector(0, -10, 0), length=1, height=1, width=1, visible=False)
        T5 = text(text='Нагреватель', pos=vector(5, 7.5, 0.5), height=0.8, color=color.red, visible=False)
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            rate(50)

            if not self.is_run:
                break

            while ball_1_1.pos.y >= 0:
                rate(100)
                
                if not self.is_run:
                    break
                
                ball_1_1.pos.y -= 0.02


            if not self.is_run:
                break

            while ball_1_1.pos.y <= 8:
                rate(100)

                if not self.is_run:
                    break

                ball_1_1.pos.y += 0.02
            
            if not self.is_run:
                break

            mybox5.visible = True
            T5.visible = True

            while ball_1_1.color.z >= 0:
                rate(100)
                
                if not self.is_run:
                    break
                
                ball_1_1.color.x += 0.005
                ball_1_1.color.z -= 0.005
            
            if not self.is_run:
                break
            
            while ball_1_1.pos.y >= 5:
                rate(100)

                if not self.is_run:
                    break
                
                ball_1_1.pos.y -= 0.02
            
            if not self.is_run:
                break
            
            for i in range(200):
                rate(100)
                if not self.is_run:
                    break
                invisible_box.pos.x += 0.0001

            if not self.is_run:
                break
            
            mybox5.visible = False
            T5.visible = False

            while ball_1_1.pos.y <= 8:
                rate(100)

                if not self.is_run:
                    break

                ball_1_1.pos.y += 0.02
            
            if not self.is_run:
                break
            
            while ball_1_1.color.x >= 0:
                rate(100)
                
                if not self.is_run:
                    break

                ball_1_1.color.x -= 0.005
                ball_1_1.color.z += 0.005    
