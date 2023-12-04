import constants
from experiments import Experiment
from vpython import *


class ElectricityExperiment(Experiment):
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

        mybox1 = box(pos=vector(-10, 0, 0), length=2, height=22, width=1, opacity=0.3, color=color.cyan)
        mybox2 = box(pos=vector(10, 0, 0), length=2, height=22, width=1, opacity=0.3, color=color.cyan)
        mybox3_1 = box(pos=vector(-6, -10, 0), length=6, height=2, width=1, opacity=0.3, color=color.cyan)
        mybox3_2 = box(pos=vector(6, -10, 0), length=6, height=2, width=1, opacity=0.3, color=color.cyan)
        mybox3_3 = box(pos=vector(0, -10, 0), length=6, height=2, width=1, opacity=0.3, color=color.cyan,
                       up=vector(1, 0, 0))
        mybox4 = box(pos=vector(0, 10, 0), length=18, height=2, width=1, opacity=0.3, color=color.cyan)
        mybox5 = box(pos=vector(0, 10, 0), length=8, height=4, width=4, color=color.red)
        mybox6 = box(pos=vector(10, 0, 0), length=4, height=8, width=4, color=color.blue)
        ball_1 = sphere(pos=vector(10, 10, 0), radius=0.5, color=color.blue)
        ball_2 = sphere(pos=vector(-10, 10, 0), radius=0.5, color=color.blue)
        ball_3 = sphere(pos=vector(-10, -10, 0), radius=0.5, color=color.blue)
        ball_4 = sphere(pos=vector(10, -10, 0), radius=0.5, color=color.blue)
        T = text(text='+  -', pos=vector(-2.5, 8.8, 1.5), height=3, color=color.white)
        pos = 1

        for i in range(157):
            rate(300)
            mybox3_3.rotate(angle=0.01, axis=vector(0, 0, 1), origin=mybox3_3.pos)

        while True:
            rate(500)
            if ball_1.pos.x >= 10 and ball_1.pos.y >= 10:
                pos = 1
            if ball_1.pos.x >= 10 and ball_1.pos.y <= -10:
                pos = 2
            if ball_1.pos.x <= -10 and ball_1.pos.y <= -10:
                pos = 3
            if ball_1.pos.x <= -10 and ball_1.pos.y >= 10:
                pos = 4
            if pos == 1:
                ball_1.pos.y -= 0.01
                ball_2.pos.x += 0.01
                ball_3.pos.y += 0.01
                ball_4.pos.x -= 0.01
            if pos == 2:
                ball_1.pos.x -= 0.01
                ball_2.pos.y -= 0.01
                ball_3.pos.x += 0.01
                ball_4.pos.y += 0.01
            if pos == 3:
                ball_1.pos.y += 0.01
                ball_2.pos.x -= 0.01
                ball_3.pos.y -= 0.01
                ball_4.pos.x += 0.01
            if pos == 4:
                ball_1.pos.x += 0.01
                ball_2.pos.y += 0.01
                ball_3.pos.x -= 0.01
                ball_4.pos.y -= 0.01
