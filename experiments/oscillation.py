from math import cos, pi, sin

import constants
from experiments import Experiment
from vpython import *


class OscillationExperiment(Experiment):
    def __init__(self):
        super().__init__()

    def run(self):
        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        pendulums = []
        hinge = cylinder(pos=vec(0, 10, -15), axis=vec(0, 0, 1), size=vec(30, .8, .8), color=vec(.5, .5, .8))

        for i in range(15):
            pendulum = sphere(radius=0.8, color=color.hsv_to_rgb(vec(i / 20, 0.6, 0.8)))
            pendulum.theta0 = -0.6
            pendulum.period = 60 / (51 + i)
            pendulum.wire = cylinder()
            pendulum.wire.color = pendulum.color
            pendulum.wire.pos = hinge.pos + vec(0, 0, i + .5) * hinge.size.x / 15
            pendulum.wire.size = vec(15 * pendulum.period * pendulum.period, .1, .1)
            pendulums.append(pendulum)

        time = 0
        delta_time = 0.001

        while True:
            rate(1000)

            for pendulum in pendulums:
                theta = pendulum.theta0 * cos(2 * pi * time / pendulum.period)
                pendulum.wire.axis = pendulum.wire.size.x * vec(sin(theta), -cos(theta), 0)
                pendulum.pos = pendulum.wire.pos + pendulum.wire.axis

            time = time + delta_time
