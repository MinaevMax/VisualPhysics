import constants
from experiments import Experiment
from vpython import *


class InelasticCollisionExperiment(Experiment):
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

        rod1 = cylinder(pos=vector(0, 1.5, 0), axis=vector(2, 0, 0), radius=1, texture=textures.metal)
        rod2 = cylinder(pos=vector(0, 1.5, -10), axis=vector(2, 0, 0), radius=1, texture=textures.metal)
        my = box(pos=vector(0, 0, 0), length=10, height=1, width=25, texture=textures.rock)
        b1 = vector(0, 1.5, 0)
        b2 = vector(0, 1.5, -10)

        while True:
            rate(1000)

            while b2.z + 2 < b1.z:
                rate(200)
                rod2.rotate(angle=0.02, axis=vector(1, 0, 0), origin=rod2.pos)
                rod2.pos = b2
                b2.z += 0.016

            while b1.z < 10:
                rate(200)
                rod1.rotate(angle=0.01, axis=vector(1, 0, 0), origin=rod1.pos)
                rod2.rotate(angle=0.01, axis=vector(1, 0, 0), origin=rod2.pos)
                rod2.pos = b2
                b2.z += 0.008
                rod1.pos = b1
                b1.z += 0.008

            b1.z = 0
            b2.z = -10
            rod1.pos = b1
            rod2.pos = b2