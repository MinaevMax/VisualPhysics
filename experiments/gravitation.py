from i18n import t

import constants
from experiments import Experiment
from vpython import *


class GravitationExperiment(Experiment):
    def __init__(self):
        super().__init__()

    def _repeat(self):
        self.ball.pos.y = 10
        self.u = 0
        self._puk()

    def _puk(self):
        for i in range(200):
            rate(1000)
            self.invisible_box.pos.x += 0.0001

        while self.ball.pos.y >= -8:
            for i in range(200):
                rate(1000)
                self.invisible_box.pos.x += 0.0001

            self.u += 0.04
            self.ball.pos.y -= self.u

        for i in range(200):
            rate(1000)
            self.invisible_box.pos.x += 0.0001

    def run(self):
        super()._init_i18n()

        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        self.ball = sphere(pos=vector(0, 10, 0), radius=0.5, color=color.red)
        self.invisible_box = box(pos=vector(0, -10, 0), length=1, height=1, width=1, visible=False)
        self.u = 0

        box(pos=vector(0, -9.6, 0), length=10, height=1, width=10, texture=textures.metal)
        button(text=t('repeat'), bind=self._repeat)

        self._puk()

        while True:
            pass




