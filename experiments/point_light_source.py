import constants
from experiments import Experiment
from vpython import *


class PointLightSourceExperiment(Experiment):
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

        m1 = box(pos=vector(0, 0, 0), length=1, height=8, width=3, color=color.cyan)
        m2 = box(pos=vector(10, 0, 0), length=2, height=25, width=3, color=color.cyan)
        ball_1_1 = sphere(pos=vector(-15, 0, 0), radius=0.3, color=color.red, make_trail=True)
        ball_1_2 = sphere(pos=vector(-15, 0, 0), radius=0.5, color=color.yellow)
        xb = 0
        yb = -0.025

        while True:
            rate(1000)

            while yb <= 0.025:
                xb = 0.05
                yb += 0.001
                while not (0 <= ball_1_1.pos.x <= 0.01 and -4.2 <= ball_1_1.pos.y <= 4.2) and not (
                        10 <= ball_1_1.pos.x <= 10.5 and -40 <= ball_1_1.pos.y <= 40):
                    rate(500)

                    ball_1_1.pos.x += xb
                    ball_1_1.pos.y += yb

                ball_1_1.make_trail = False
                ball_1_1.pos.x = -15
                ball_1_1.pos.y = 0
                ball_1_1.make_trail = True
