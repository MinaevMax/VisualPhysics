import constants
from experiments import Experiment
from vpython import *


class RefractionExperiment(Experiment):
    def __init__(self):
        """Init.

            Initializing the experiment.
        """
        super().__init__()

    def run(self):
        """Run.

            Running the experiment in 3D model.
        """
        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        ball_1_1 = sphere(pos=vector(0, 8, -8), radius=0.3, color=color.red, make_trail=True, retain=100)
        my = box(pos=vector(0, 0, -2), opacity=0.3, length=-8, height=5, width=20, color=color.cyan)
        b = vector(0, 8, -8)
        pl1 = -0.008
        pl2 = 0.008
        td = 1

        while True:
            rate(200)

            ball_1_1.pos = b
            b.z += pl2
            b.y += pl1

            if ball_1_1.pos.y + 0.3 < my.pos.y + 3 and td == 1:
                pl2 = 0.002

            if ball_1_1.pos.y < my.pos.y - 2.5 and td == 1:
                pl2 = 0.008

            if ball_1_1.pos.y < -8 and td == 1:
                pl2 = -0.008
                pl1 = 0.008
                td = 2

            if ball_1_1.pos.y > my.pos.y - 2.5 and td == 2:
                pl2 = -0.002

            if ball_1_1.pos.y + 0.3 > my.pos.y + 3 and td == 2:
                pl2 = -0.008
                pl1 = 0.008

            if ball_1_1.pos.y > 8 and td == 2:
                pl1 = -0.008
                pl2 = 0.008
                td = 1
