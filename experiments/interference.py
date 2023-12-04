import constants
from experiments import Experiment
from vpython import *


class InterferenceExperiment(Experiment):
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

        # 2 шарика в начале
        ball_1 = sphere(pos=vector(5, 8, 0), radius=0.3, color=color.red, make_trail=True, retain=20)
        ball_2 = sphere(pos=vector(-5, 8, 0), radius=0.3, color=color.red, make_trail=True, retain=20)
        b_1 = vector(5, 8, 0)
        b_2 = vector(-5, 8, 0)

        box(pos=vector(0, 0, -2), opacity=0.3, length=50, height=0.1, width=50, color=color.cyan)

        # Списки колебаний(колец) для первого и второго шарика
        ri_1 = []
        ri_2 = []
        ch = 0
        n = 0

        # Первые кольца по умолчания
        ri_1.append(
            ring(pos=vector(5, 0, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red, visible=False))
        ri_2.append(
            ring(pos=vector(-5, 0, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red, visible=False))

        while True:
            # Падение двух шариков
            while b_1.y >= 0.1:
                rate(300)

                ball_1.pos = b_1
                ball_2.pos = b_2
                b_1.y -= 0.008
                b_2.y -= 0.008

            ri_1[0].visible = True
            ri_2[0].visible = True

            # Начало колебаний
            while True:
                rate(400)

                for i in range(len(ri_1)):
                    ri_1[i].radius += 0.008
                    ri_2[i].radius += 0.008

                ch += 0.008

                # Добавление колец при первом прохождении
                if ch > 5 and len(ri_1) <= 3:
                    ch = 0
                    ri_1.append(ring(pos=vector(5, 0, 0), axis=vector(0, 1, 0),
                                     radius=0.5, thickness=0.1, color=color.red))
                    ri_2.append(ring(pos=vector(-5, 0, 0), axis=vector(0, 1, 0),
                                     radius=0.5, thickness=0.1, color=color.red))
                # При достижении 4‑х колец новые перестают добавляться и просто меняется значение радиуса крайнего
                # кольца
                elif ch > 5 and len(ri_1) > 3:
                    ch = 0
                    ri_1[n].radius = 0.5
                    ri_2[n].radius = 0.5

                    if n + 1 < len(ri_1):
                        n += 1
                    else:
                        n = 0
