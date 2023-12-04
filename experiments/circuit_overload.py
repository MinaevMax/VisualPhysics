import constants
from experiments import Experiment
from vpython import *


class CircuitOverloadExperiment(Experiment):
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

        box_1 = box(pos=vector(-10, 0, 0), length=2, height=22, width=1, opacity=0.3, color=color.blue)
        box_2 = box(pos=vector(10, 0, 0), length=2, height=22, width=1, opacity=0.3, color=color.blue)
        box_3 = box(pos=vector(-6, -10, 0), length=6, height=2, width=1, opacity=0.3, color=color.blue)
        box_4 = box(pos=vector(6, -10, 0), length=6, height=2, width=1, opacity=0.3, color=color.blue)
        box_5 = box(pos=vector(0, -10, 0), length=6, height=2, width=1, opacity=0.3, color=color.blue,
                    up=vector(1, 0, 0))
        box_7 = box(pos=vector(0, 10, 0), length=18, height=2, width=1, opacity=0.3, color=color.blue)
        box_8 = box(pos=vector(0, 10, 0), length=8, height=4, width=4, color=color.red)
        box_9 = box(pos=vector(10, 0, 0), length=4, height=8, width=4, color=color.blue)
        sphere_top = sphere(pos=vector(-10, 5, 0), radius=4, color=color.blue)
        sphere_bottom = sphere(pos=vector(-10, -5, 0), radius=4, color=color.blue)
        ball_1 = sphere(pos=vector(10, 10, 0), radius=0.5, color=color.blue)
        ball_2 = sphere(pos=vector(-10, 10, 0), radius=0.5, color=color.blue)
        ball_3 = sphere(pos=vector(-10, -10, 0), radius=0.5, color=color.blue)
        ball_4 = sphere(pos=vector(10, -10, 0), radius=0.5, color=color.blue)
        pos = 1

        text(text='+  -', pos=vector(-2.5, 8.8, 1.5), height=3, color=color.white)

        for i in range(157):
            rate(300)
            box_5.rotate(angle=0.01, axis=vector(0, 0, 1), origin=box_5.pos)

        while box_1.color.x < 10:
            rate(500)

            sphere_top.color.z -= 0.1
            sphere_top.color.x += 0.1
            sphere_top.color.y += 0.1
            sphere_bottom.color.z -= 0.1
            sphere_bottom.color.x += 0.1
            sphere_bottom.color.y += 0.1
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
            box_1.color.z -= 0.01
            box_1.color.x += 0.01
            box_2.color.z -= 0.01
            box_2.color.x += 0.01
            box_3.color.z -= 0.01
            box_3.color.x += 0.01
            box_4.color.z -= 0.01
            box_4.color.x += 0.01
            box_5.color.z -= 0.01
            box_5.color.x += 0.01
            box_7.color.z -= 0.01
            box_7.color.x += 0.01

        for i in range(157):
            rate(300)
            box_5.rotate(angle=0.01, axis=vector(0, 0, 1), origin=box_5.pos)

        while box_1.color.x > 0:
            rate(500)

            box_1.color.z += 0.01
            box_1.color.x -= 0.01
            box_2.color.z += 0.01
            box_2.color.x -= 0.01
            box_3.color.z += 0.01
            box_3.color.x -= 0.01
            box_4.color.z += 0.01
            box_4.color.x -= 0.01
            box_5.color.z += 0.01
            box_5.color.x -= 0.01
            box_7.color.z += 0.01
            box_7.color.x -= 0.01
            sphere_top.color.z += 0.1
            sphere_top.color.x -= 0.1
            sphere_top.color.y -= 0.1
            sphere_bottom.color.z += 0.1
            sphere_bottom.color.x -= 0.1
            sphere_bottom.color.y -= 0.1

        while True:
            pass
