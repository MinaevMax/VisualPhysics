import constants
from experiments import Experiment
from vpython import *


class ThermalTransitionExperiment(Experiment):
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

        m1 = box(pos=vector(0, 0, 0), length=10, height=0.5, width=25, color=color.blue)
        m2 = box(pos=vector(0, 4.5, 0), length=10, height=0.5, width=25, color=color.blue)

        while True:
            rate(100)

            while m1.pos.y + m1.height < m2.pos.y:
                rate(200)

                m2.pos.y -= 0.05

            for i in range(3):
                while m2.pos.z < 5:
                    rate(200)

                    m2.pos.z += 0.03
                    m1.color.z -= 0.001
                    m1.color.x += 0.001
                    m2.color.z -= 0.001
                    m2.color.x += 0.001

                while m2.pos.z > -5:
                    rate(200)

                    m2.pos.z -= 0.03
                    m1.color.z -= 0.001
                    m1.color.x += 0.001
                    m2.color.z -= 0.001
                    m2.color.x += 0.001

                while m2.pos.z < 0:
                    rate(200)

                    m2.pos.z += 0.03
                    m1.color.z -= 0.001
                    m1.color.x += 0.001
                    m2.color.z -= 0.001
                    m2.color.x += 0.001

            while m2.pos.y < 4.5:
                rate(200)

                m2.pos.y += 0.03

            while m2.color.x >= 0:
                rate(200)

                m1.color.z += 0.001
                m1.color.x -= 0.001
                m2.color.z += 0.001
                m2.color.x -= 0.001
