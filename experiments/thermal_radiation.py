import constants
from experiments import Experiment
from vpython import *


class ThermalRadiationExperiment(Experiment):
    def __init__(self):
        super().__init__()

    def run(self):
        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        ball_1 = sphere(pos=vector(0, 0, 0), radius=0.5, opacity=0.4, color=color.red)
        ball_2 = sphere(pos=vector(-1, 0, 0), radius=0.2, color=color.blue)
        ball_3 = sphere(pos=vector(1, 0, 0), radius=0.2, color=color.blue)
        ri = []
        ch = 0
        n = 0
        ri.append(
            ring(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.01, color=color.red, visible=True))

        while len(ri) <= 2:
            rate(50)

            for i in range(len(ri)):
                ri[i].radius += 0.008

            ch += 0.01

            if ch > 0.5:
                ch = 0
                ri.append(ring(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.01, color=color.red))

        while ball_2.color.z > 0:
            rate(50)

            for i in range(len(ri)):
                ri[i].radius += 0.008

            ball_2.color.x += 0.005
            ball_2.color.z -= 0.005
            ball_3.color.x += 0.005
            ball_3.color.z -= 0.005
            ch += 0.01
            if ch > 0.5:
                ch = 0
                ri[n].radius = 0.5
                if n + 1 < len(ri):
                    n += 1
                else:
                    n = 0

        while True:
            pass
