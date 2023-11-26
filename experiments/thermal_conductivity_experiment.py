from vpython import *
from multiprocessing import Process

class ThermalConductivityExperiment(Process):

    def __init__(self, value):
        super(ThermalConductivityExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        mybox1 = box(pos=vector(-10, 0.5, 0), length=1, height=10, width=1, texture=textures.metal)
        mybox2 = box(pos=vector(-10, -4, 0), length=3, height=1, width=3, texture=textures.metal)
        mybox3 = box(pos=vector(10, 0.5, 0), length=1, height=10, width=1, texture=textures.metal)
        mybox4 = box(pos=vector(10, -4, 0), length=3, height=1, width=3, texture=textures.metal)
        rod = cylinder(pos=vector(-10, 6, 0), axis=vector(22, 0, 0), radius=0.5, color=color.blue)
        rod1 = cylinder(pos=vector(12, 6, 0), axis=vector(0, 0, 0), radius=0.52, color=color.red, visible=False)
        mybox5 = box(pos=vector(12, 4, 0), length=2, height=2, width=2, color=color.red, visible=False)
        T5 = text(text='Нагреватель', pos=vector(13.5, 3.5, 0.5), height=0.8, color=color.red, visible=False)
        pointer1 = arrow(pos=vector(5, 5.5, 0), axis=vector(0, -4, 0), color=color.orange)
        pointer2 = arrow(pos=vector(0, 5.5, 0), axis=vector(0, -4, 0), color=color.orange)
        pointer3 = arrow(pos=vector(-5, 5.5, 0), axis=vector(0, -4, 0), color=color.orange)
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            rate(200)

            if not self.is_run:
                break
                
            mybox5.visible = True
            T5.visible = True
            rod1.visible = True
            
            while rod1.axis.x >= -22.1:
                rate(200)

                if not self.is_run:
                    break

                if rod1.axis.x <= -7 and pointer1.pos.y >= -0.5:
                    pointer1.pos.y -= 0.02
                if rod1.axis.x <= -12 and pointer2.pos.y >= -0.5:
                    pointer2.pos.y -= 0.02
                if rod1.axis.x <= -17 and pointer3.pos.y >= -0.5:
                    pointer3.pos.y -= 0.02
                rod1.axis.x -= 0.01
            
            if not self.is_run:
                break
            
            mybox5.visible = False
            T5.visible = False
            rod1.axis.x = 0
            pointer1.pos.y = 5.5
            pointer2.pos.y = 5.5
            pointer3.pos.y = 5.5
