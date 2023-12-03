import constants
from experiments import Experiment
from vpython import *


class DiffractionExperiment(Experiment):
    def __init__(self):
        super().__init__()

    def run(self):
        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        box(pos=vector(0, 10, 0), opacity=0.3, length=18, height=0.1, width=41, color=color.cyan)
        box(pos=vector(-20, 10, 0), opacity=0.3, length=18, height=0.1, width=41, color=color.cyan)
        box(pos=vector(20, 10, 0), opacity=0.3, length=18, height=0.1, width=41, color=color.cyan)
        box(pos=vector(0, -10, 0), opacity=0.3, length=60, height=0.1, width=41, color=color.cyan)
        box(pos=vector(14, 26, 0), opacity=0.3, length=26, height=0.1, width=41, color=color.cyan)
        box(pos=vector(-14, 26, 0), opacity=0.3, length=26, height=0.1, width=41, color=color.cyan)

        ri_1 = []
        ri_2 = []
        ri_3 = []
        ch_1 = 0
        ch_2 = 0
        n_1 = 0
        n_2 = 0

        ri_1.append(ring(pos=vector(10, 10, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red,
                         visible=False))
        ri_2.append(ring(pos=vector(-10, 10, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red,
                         visible=False))
        ri_3.append(
            ring(pos=vector(0, 26, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red, visible=True))

        while len(ri_3) <= 4:
            rate(400)

            for i in range(len(ri_3)):
                ri_3[i].radius += 0.008
                ri_3[i].pos.y -= 0.008

            ch_2 += 0.01

            if ch_2 > 5:
                ch_2 = 0

                ri_3.append(
                    ring(pos=vector(0, 26, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red))

        while True:
            ri_1[0].visible = True
            ri_2[0].visible = True

            while True:
                rate(400)

                for i in range(len(ri_3)):
                    if i < len(ri_1):
                        ri_1[i].radius += 0.008
                        ri_2[i].radius += 0.008
                        ri_1[i].pos.y -= 0.008
                        ri_2[i].pos.y -= 0.008

                    ri_3[i].radius += 0.008
                    ri_3[i].pos.y -= 0.008

                ch_1 += 0.01

                if ch_1 > 5 and len(ri_1) <= 4:
                    ch_1 = 0

                    ri_1.append(
                        ring(pos=vector(10, 10, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red))
                    ri_2.append(
                        ring(pos=vector(-10, 10, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red))

                if ch_1 > 5 and len(ri_1) > 4:
                    ch_1 = 0
                    ri_1[n_2].radius = 0.5
                    ri_2[n_2].radius = 0.5
                    ri_1[n_2].pos.y = 10
                    ri_2[n_2].pos.y = 10

                    if n_2 + 1 < len(ri_1):
                        n_2 += 1
                    else:
                        n_2 = 0

                if ri_3[n_1].pos.y <= 10:
                    ri_3[n_1].radius = 0.5
                    ri_3[n_1].pos.y = 26

                    if n_1 + 1 < len(ri_3):
                        n_1 += 1
                    else:
                        n_1 = 0
