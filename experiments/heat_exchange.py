import constants
from experiments import Experiment
from vpython import *


class HeatExchangeExperiment(Experiment):
    def __init__(self):
        super().__init__()

    def run(self):
        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        ball_1 = sphere(pos=vector(-1.5, 0, 0), radius=0.5, opacity=0.4, color=color.red)
        ball_2 = sphere(pos=vector(1.5, 0, 0), radius=0.5, opacity=0.4, color=color.blue)
        ri_1 = []
        ri_2 = []
        ch = 0
        n = 0

        ri_1.append(ring(pos=vector(-1.5, 0, 0), axis=vector(1, 0, 0), radius=0.5, thickness=0.02, color=color.red,
                         visible=True))
        ri_2.append(ring(pos=vector(1.5, 0, 0), axis=vector(1, 0, 0), radius=0.5, thickness=0.02, color=color.blue,
                         visible=True))

        while len(ri_1) <= 2:
            rate(50)

            for i in range(len(ri_1)):
                ri_1[i].pos.x += 0.01
                ri_2[i].pos.x -= 0.01

            ch += 0.01
            if ch > 1:
                ch = 0

                ri_1.append(
                    ring(pos=vector(-1.5, 0, 0), axis=vector(1, 0, 0), radius=0.5, thickness=0.02, color=color.red))
                ri_2.append(
                    ring(pos=vector(1.5, 0, 0), axis=vector(1, 0, 0), radius=0.5, thickness=0.02, color=color.blue))

        while ball_1.color.x >= ball_2.color.x:
            rate(50)

            for i in range(len(ri_1)):
                ri_1[i].pos.x += 0.01
                ri_2[i].pos.x -= 0.01

            ch += 0.01
            if ch > 1:
                ch = 0
                ri_1[n].pos.x = -1.5
                ri_1[n].color = ball_1.color
                ri_2[n].pos.x = 1.5
                ri_2[n].color = ball_2.color

                if n + 1 < len(ri_1):
                    n += 1
                else:
                    n = 0

            ball_1.color.x -= 0.001
            ball_1.color.z += 0.001
            ball_2.color.x += 0.001
            ball_2.color.z -= 0.001

        ri_1[0].visible = False
        ri_1[1].visible = False
        ri_1[2].visible = False
        ri_2[0].visible = False
        ri_2[1].visible = False
        ri_2[2].visible = False

        while True:
            pass
