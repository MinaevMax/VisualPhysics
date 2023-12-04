import constants
from experiments import Experiment
from vpython import *


class RealLightSourceExperiment(Experiment):
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

        m2 = box(pos=vector(10, 0, 0), length=2, height=25, width=3, color=color.cyan)
        ball_1_1 = sphere(pos=vector(-15, -3, 0), radius=0.3, color=color.red, make_trail=True)
        ball_1_3 = sphere(pos=vector(-15, 3, 0), radius=0.3, color=color.red, make_trail=True)
        ball_1_2 = sphere(pos=vector(-15, 0, 0), radius=3, color=color.yellow)
        m1 = box(pos=vector(0, 0, 0), length=1.5, height=8, width=3, color=color.cyan)
        xb1 = 0.05
        yb1 = -0.019
        xb2 = 0.05
        yb2 = 0.019
        flag = 0

        while True:
            rate(1000)
            yb1 += 0.0008
            yb2 -= 0.0008

            while yb1 <= 0.031:
                while flag == 0:
                    rate(500)

                    if 0 <= ball_1_1.pos.x <= 0.5 and -4.2 <= ball_1_1.pos.y <= 4.2 or 10 <= ball_1_1.pos.x <= 10.5 and -40 <= ball_1_1.pos.y <= 40:
                        flag = 1
                    elif 0 <= ball_1_3.pos.x <= 0.5 and -4.2 <= ball_1_3.pos.y <= 4.2 or 10 <= ball_1_3.pos.x <= 10.5 and -40 <= ball_1_3.pos.y <= 40:
                        flag = 3

                    ball_1_1.pos.x += xb1
                    ball_1_1.pos.y += yb1
                    ball_1_3.pos.x += xb2
                    ball_1_3.pos.y += yb2

                if flag == 1:
                    yb1 += 0.002
                    ball_1_1.make_trail = False
                    ball_1_1.pos.x = -15
                    ball_1_1.pos.y = -3
                    ball_1_1.make_trail = True
                elif flag == 3:
                    yb2 -= 0.002
                    ball_1_3.make_trail = False
                    ball_1_3.pos.x = -15
                    ball_1_3.pos.y = 3
                    ball_1_3.make_trail = True
                flag = 0
