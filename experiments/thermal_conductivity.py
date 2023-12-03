import constants
from experiments import Experiment
from vpython import *


class ThermalConductivityExperiment(Experiment):
    def __init__(self):
        super().__init__()

    def run(self):
        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        box(pos=vector(-10, 0.5, 0), length=1, height=10, width=1, texture=textures.metal)
        box(pos=vector(-10, -4, 0), length=3, height=1, width=3, texture=textures.metal)
        box(pos=vector(10, 0.5, 0), length=1, height=10, width=1, texture=textures.metal)
        box(pos=vector(10, -4, 0), length=3, height=1, width=3, texture=textures.metal)
        cylinder(pos=vector(-10, 6, 0), axis=vector(22, 0, 0), radius=0.5, color=color.blue)
        rod1 = cylinder(pos=vector(12, 6, 0), axis=vector(0, 0, 0), radius=0.52, color=color.red, visible=False)
        mybox5 = box(pos=vector(12, 4, 0), length=2, height=2, width=2, color=color.red, visible=False)
        T5 = text(text='Нагреватель', pos=vector(13.5, 3.5, 0.5), height=0.8, color=color.red, visible=False)
        pointer1 = arrow(pos=vector(5, 5.5, 0), axis=vector(0, -4, 0), color=color.orange)
        pointer2 = arrow(pos=vector(0, 5.5, 0), axis=vector(0, -4, 0), color=color.orange)
        pointer3 = arrow(pos=vector(-5, 5.5, 0), axis=vector(0, -4, 0), color=color.orange)

        while True:
            rate(200)

            mybox5.visible = True
            T5.visible = True
            rod1.visible = True

            while rod1.axis.x >= -22.1:
                rate(200)

                if rod1.axis.x <= -7 and pointer1.pos.y >= -0.5:
                    pointer1.pos.y -= 0.02
                if rod1.axis.x <= -12 and pointer2.pos.y >= -0.5:
                    pointer2.pos.y -= 0.02
                if rod1.axis.x <= -17 and pointer3.pos.y >= -0.5:
                    pointer3.pos.y -= 0.02
                rod1.axis.x -= 0.01

            mybox5.visible = False
            T5.visible = False
            rod1.axis.x = 0
            pointer1.pos.y = 5.5
            pointer2.pos.y = 5.5
            pointer3.pos.y = 5.5
