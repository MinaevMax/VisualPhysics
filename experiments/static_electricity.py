import constants
from experiments import Experiment
from vpython import *


class StaticElectricityExperiment(Experiment):
    def __init__(self):
        super().__init__()

    def run(self):
        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        ball_1_1 = sphere(pos=vector(-2, 1, 1), radius=0.3, color=color.cyan)
        ball_1_2 = sphere(pos=vector(0, 1, -1), radius=0.3, color=color.cyan)
        ball_1_3 = sphere(pos=vector(2, 1, 1), radius=0.3, color=color.cyan)
        ball_2_1 = sphere(pos=vector(-2, 4, -1), radius=0.3, color=color.cyan)
        ball_2_2 = sphere(pos=vector(0, 4, 1), radius=0.3, color=color.cyan)
        ball_2_3 = sphere(pos=vector(2, 4, -1), radius=0.3, color=color.cyan)
        m1 = box(pos=vector(0, 0.5, 0), length=10, height=0.5, width=25, texture=textures.rug)
        m2 = box(pos=vector(0, 4.5, 0), length=10, height=0.5, width=25, texture=textures.rug, opacity=0.65)

        while True:
            rate(1000)

            while m1.pos.y + m1.height * 2 < m2.pos.y:
                rate(200)
                m2.pos.y -= 0.01
                ball_2_1.pos.y -= 0.01
                ball_2_2.pos.y -= 0.01
                ball_2_3.pos.y -= 0.01

            while m2.pos.z < 5:
                rate(200)
                m2.pos.z += 0.01
                ball_2_1.pos.z += 0.01
                ball_2_2.pos.z += 0.01
                ball_2_3.pos.z += 0.01

            while m2.pos.z > -5:
                rate(200)
                m2.pos.z -= 0.01
                ball_2_1.pos.z -= 0.01
                ball_2_2.pos.z -= 0.01
                ball_2_3.pos.z -= 0.01

            while m2.pos.z < 0:
                rate(200)
                m2.pos.z += 0.01
                ball_2_1.pos.z += 0.01
                ball_2_2.pos.z += 0.01
                ball_2_3.pos.z += 0.01

            while m2.pos.y < 4.5:
                rate(200)
                m2.pos.y += 0.01
                ball_2_1.pos.y += 0.01
                ball_1_1.pos.y += 0.01
                ball_2_3.pos.y += 0.01
                ball_2_2.pos.y += 0.01
                ball_1_3.pos.y += 0.01

            ball_1_1.pos.y = 1
            ball_1_3.pos.y = 1
