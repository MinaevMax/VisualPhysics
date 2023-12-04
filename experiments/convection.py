import constants
from experiments import Experiment
from vpython import *


class ConvectionExperiment(Experiment):
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

        c = curve()
        c.append(pos=vector(-11, -11, 0), color=color.red, radius=0.5)
        c.append(pos=vector(-11, 11, 0), color=color.red, radius=0.5)
        c.append(pos=vector(11, 11, 0), color=color.yellow, radius=0.5)
        c.append(pos=vector(11, -11, 0), color=color.blue, radius=0.5)
        c.append(pos=vector(-11, -11, 0), color=color.red, radius=0.5)

        ball_1 = sphere(pos=vector(10, 10, 0), radius=0.5, color=color.yellow)
        ball_2 = sphere(pos=vector(-10, 10, 0), radius=0.5, color=color.red)
        ball_3 = sphere(pos=vector(-10, -10, 0), radius=0.5, color=color.red)
        ball_4 = sphere(pos=vector(10, -10, 0), radius=0.5, color=color.blue)

        box(pos=vector(-12, 0, 0), length=2, height=26, width=1, opacity=0.3, color=color.blue)
        box(pos=vector(12, 0, 0), length=2, height=26, width=1, opacity=0.3, color=color.blue)
        box(pos=vector(0, 12, 0), length=22, height=2, width=1, opacity=0.3, color=color.blue)
        box(pos=vector(0, -12, 0), length=22, height=2, width=1, opacity=0.3, color=color.blue)
        box(pos=vector(-12, -12, 0), length=2, height=2, width=2, color=color.red)
        text(text='Холодная среда', pos=vector(-5, 11.5, 0.5), height=1, color=color.black)
        text(text='Холодная среда', pos=vector(-5, -12.5, 0.5), height=1, color=color.black)
        text(text='Холодная среда', pos=vector(-11.5, -5, 0.5), axis=vector(0, 1, 0), height=1, color=color.black)
        text(text='Холодная среда', pos=vector(11.5, 5, 0.5), axis=vector(0, -1, 0), height=1, color=color.black)
        text(text='Нагреватель', pos=vector(-15, -14, 0.5), height=0.8, color=color.red)

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
                ball_3.color = color.red

                ball_2.color.y += 0.0005

                ball_1.color.y -= 0.0005
                ball_1.color.x -= 0.0005
                ball_1.color.z += 0.0005

                ball_4.color.x += 0.0005
                ball_4.color.z -= 0.0005

                ball_1.pos.y -= 0.01
                ball_2.pos.x += 0.01
                ball_3.pos.y += 0.01
                ball_4.pos.x -= 0.01
            if pos == 2:
                ball_4.color = color.red

                ball_3.color.y += 0.0005

                ball_2.color.y -= 0.0005
                ball_2.color.x -= 0.0005
                ball_2.color.z += 0.0005

                ball_1.color.x += 0.0005
                ball_1.color.z -= 0.0005

                ball_1.pos.x -= 0.01
                ball_2.pos.y -= 0.01
                ball_3.pos.x += 0.01
                ball_4.pos.y += 0.01
            if pos == 3:
                ball_1.color = color.red

                ball_4.color.y += 0.0005

                ball_3.color.y -= 0.0005
                ball_3.color.x -= 0.0005
                ball_3.color.z += 0.0005

                ball_2.color.x += 0.0005
                ball_2.color.z -= 0.0005

                ball_1.pos.y += 0.01
                ball_2.pos.x -= 0.01
                ball_3.pos.y -= 0.01
                ball_4.pos.x += 0.01
            if pos == 4:
                ball_2.color = color.red

                ball_1.color.y += 0.0005

                ball_4.color.y -= 0.0005
                ball_4.color.x -= 0.0005
                ball_4.color.z += 0.0005

                ball_3.color.x += 0.0005
                ball_3.color.z -= 0.0005

                ball_1.pos.x += 0.01
                ball_2.pos.y += 0.01
                ball_3.pos.x -= 0.01
                ball_4.pos.y -= 0.01
