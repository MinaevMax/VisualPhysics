import constants
from experiments import Experiment
from vpython import *


class ExpansionExperiment(Experiment):
    def __init__(self):
        super().__init__()

    def run(self):
        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        ball_1_1 = sphere(pos=vector(0, 8, 0), radius=2, color=color.blue)
        mybox1 = box(pos=vector(-2.5, 0.5, 0), length=1, height=10, width=1, texture=textures.metal)
        mybox2 = box(pos=vector(-2.5, -4, 0), length=3, height=1, width=3, texture=textures.metal)
        ring(pos=vector(0, 5, 0), axis=vector(0, 1, 0), radius=2.05, thickness=0.1, texture=textures.metal)
        mybox5 = box(pos=vector(3, 8, 0), length=2, height=2, width=2, color=color.red, visible=False)
        invisible_box = box(pos=vector(0, -10, 0), length=1, height=1, width=1, visible=False)
        T5 = text(text='Нагреватель', pos=vector(5, 7.5, 0.5), height=0.8, color=color.red, visible=False)

        while True:
            rate(50)

            while ball_1_1.pos.y >= 0:
                rate(100)
                ball_1_1.pos.y -= 0.02

            while ball_1_1.pos.y <= 8:
                rate(100)
                ball_1_1.pos.y += 0.02

            mybox5.visible = True
            T5.visible = True

            while ball_1_1.color.z >= 0:
                rate(100)
                ball_1_1.color.x += 0.005
                ball_1_1.color.z -= 0.005

            while ball_1_1.pos.y >= 5:
                rate(100)
                ball_1_1.pos.y -= 0.02

            for i in range(200):
                rate(100)
                invisible_box.pos.x += 0.0001

            mybox5.visible = False
            T5.visible = False

            while ball_1_1.pos.y <= 8:
                rate(100)
                ball_1_1.pos.y += 0.02

            while ball_1_1.color.x >= 0:
                rate(100)
                ball_1_1.color.x -= 0.005
                ball_1_1.color.z += 0.005
