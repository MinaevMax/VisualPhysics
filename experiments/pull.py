from math import sqrt

from i18n import t

import constants
from experiments import Experiment
from vpython import *


class PullExperiment(Experiment):
    def __init__(self):
        """Init.

            Initializing the experiment.
        """
        super().__init__()

    def _reset(self):
        """Reset.

            Reset values for restarting the experiment.
        """
        self.alpha.pos = vector(-self.xstart, self.b, 0)
        self.target.pos = vector(0, 0, 0)
        self.alpha.p = vector(sqrt(2. * self.alpha.mass * self.ke), 0, 0)
        self.target.mass = self.targetproperties[1] * self.mproton
        self.target.radius = (self.target.mass / self.mproton) ** (1. / 3.) * self.rproton
        self.target.q = self.targetproperties[0] * self.qe
        self.target.p = vector(0, 0, 0)

    def run(self):
        """Run.

            Running the experiment in 3D model.
        """
        super()._init_i18n()

        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        self.b = 15e-15
        projectileproperties = (2, 4)
        self.targetproperties = (8, 16)
        rpscale = 2
        parro_visible = 1
        range = 200e-15
        self.xstart = 0.95 * range
        kcoul = 9e9
        self.qe = 1.6e-19
        self.mproton = 1.7e-27
        self.rproton = 1.3e-15 * rpscale
        self.alpha = sphere(pos=vector(-self.xstart, self.b, 0), color=color.red, make_trail=True, interval=40,
                            retain=50)
        self.target = sphere(pos=vector(0, self.b - 0.00000000000004, 0), color=color.blue, make_trail=True,
                             interval=40, retain=50)
        self.alpha.mass = projectileproperties[1] * self.mproton
        self.alpha.radius = (self.alpha.mass / self.mproton) ** (1. / 3.) * self.rproton
        self.alpha.q = projectileproperties[0] * self.qe
        self.ke = 1e6 * self.qe
        self.alpha.p = vector(sqrt(2. * self.alpha.mass * self.ke), 0, 0)
        self.target.mass = self.targetproperties[1] * self.mproton
        self.target.radius = (self.target.mass / self.mproton) ** (1. / 3.) * self.rproton
        self.target.q = self.targetproperties[0] * self.qe
        self.target.p = vector(0, 0, 0)
        dt = (5. * self.xstart / (mag(self.alpha.p) / self.alpha.mass) / 1e5) * 10

        pscale = 40e-15 / 4e-20
        paarro = arrow(pos=self.alpha.pos, axis=self.alpha.p * pscale, color=color.cyan,
                       shaftwidth=0.5 * self.alpha.radius, fixedwidth=1, visible=parro_visible)
        ptarro = arrow(pos=self.target.pos, axis=self.target.p * pscale, color=color.magenta,
                       shaftwidth=0.5 * self.alpha.radius, fixedwidth=1, visible=parro_visible)

        button(text=t('repeat'), bind=self._reset)

        while True:
            rate(500)

            r12 = self.alpha.pos - self.target.pos
            f = -(kcoul * self.alpha.q * self.target.q / mag(r12) ** 2) * norm(r12)
            self.alpha.p = self.alpha.p + f * dt
            self.target.p = self.target.p - f * dt
            self.alpha.pos = self.alpha.pos + (self.alpha.p / self.alpha.mass) * dt
            self.target.pos = self.target.pos + (self.target.p / self.target.mass) * dt
            paarro.pos = self.alpha.pos
            paarro.axis = self.alpha.p * pscale
            ptarro.pos = self.target.pos
            ptarro.axis = self.target.p * pscale
