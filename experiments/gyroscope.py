from math import cos, pi, sin, sqrt

import constants
from experiments import Experiment
from vpython import *


class GyroscopeExperiment(Experiment):
    def __init__(self):
        super().__init__()

    def _reset(self):
        self.theta = 0.3 * pi
        self.thetadot = 0
        self.psi = 0
        self.psidot = 30
        self.phi = -pi / 2
        self.phidot = 0
        if self.pureprecession:
            a = (1 - self.I3 / self.I1) * sin(self.theta) * cos(self.theta)
            b = -(self.I3 / self.I1) * self.psidot * sin(self.theta)
            c = self.m * self.g * self.r * sin(self.theta) / self.I1
            self.phidot = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        self.gyro.axis = self.gyro.length * vector(sin(self.theta) * sin(self.phi), cos(self.theta),
                                                   sin(self.theta) * cos(self.phi))
        n = norm(self.gyro.axis)
        self.gyro.pos = 0.5 * self.l_shaft * n
        self.tip.pos = self.l_shaft * n
        self.tip.clear_trail()

    def run(self):
        canvas(
            width=constants.DEFAULT_EXPERIMENT_CANVAS_WIDTH,
            height=constants.DEFAULT_EXPERIMENT_CANVAS_HEIGHT,
            background=constants.EXPERIMENT_WIDTH_BACKGROUND_COLOR,
        )

        self.l_shaft = 1
        self.r = self.l_shaft / 2
        r_shaft = 0.03
        self.m = 1
        r_rotor = 0.4
        d_rotor = 0.1
        self.I3 = 0.5 * self.m * r_rotor ** 2
        self.I1 = self.m * self.r ** 2 + .5 * self.I3
        hpedestal = self.l_shaft
        wpedestal = 0.1
        tbase = 0.05
        wbase = 3 * wpedestal
        self.g = 9.8
        Fgrav = vector(0, -self.m * self.g, 0)
        top = vector(0, 0, 0)

        shaft = cylinder(length=self.l_shaft, radius=r_shaft, color=color.orange)
        rotor = cylinder(pos=vector(self.l_shaft / 2 - d_rotor / 2, 0, 0), axis=vector(d_rotor, 0, 0), radius=r_rotor,
                         color=color.gray(0.9))
        base = sphere(color=shaft.color, radius=r_shaft)
        end = sphere(pos=vector(self.l_shaft, 0, 0), color=shaft.color, radius=r_shaft)
        self.gyro = compound([shaft, rotor, base, end])
        self.gyro.texture = textures.metal
        self.tip = sphere(pos=shaft.axis, radius=shaft.radius / 2, make_trail=True, retain=250)
        self.tip.trail_color = color.green
        self.tip.trail_radius = 0.15 * r_shaft

        box(pos=top - vector(0, hpedestal / 2 + shaft.radius / 2, 0), height=hpedestal - shaft.radius,
            length=wpedestal, width=wpedestal, texture=textures.wood)
        box(pos=top - vector(0, hpedestal + tbase / 2, 0), height=tbase, length=wbase, width=wbase,
            texture=textures.wood)

        self.theta = 0
        self.thetadot = 0
        self.psi = 0
        self.psidot = 0
        self.phi = 0
        self.phidot = 0
        self.pureprecession = False

        self._reset()
        scene.waitfor('textures')

        t = 0
        delta_time = 0.0001
        steps = 20

        while True:
            rate(200)

            for step in range(steps):
                atheta = sin(self.theta) * cos(self.theta) * self.phidot ** 2 + (
                        self.m * self.g * self.r * sin(self.theta) - self.I3 * (
                        self.psidot + self.phidot * cos(self.theta)) * self.phidot * sin(self.theta)) / self.I1
                aphi = (self.I3 / self.I1) * (self.psidot + self.phidot * cos(self.theta)) * self.thetadot / sin(
                    self.theta) - 2 * cos(self.theta) * self.thetadot * self.phidot / sin(self.theta)
                apsi = self.phidot * self.thetadot * sin(self.theta) - aphi * cos(self.theta)

                self.thetadot += atheta * delta_time
                self.phidot += aphi * delta_time
                self.psidot += apsi * delta_time

                self.theta += self.thetadot * delta_time
                self.phi += self.phidot * delta_time
                self.psi += self.psidot * delta_time

            self.gyro.axis = self.gyro.length * vector(sin(self.theta) * sin(self.phi), cos(self.theta),
                                                       sin(self.theta) * cos(self.phi))

            self.gyro.rotate(angle=self.psidot * delta_time * steps)
            a = norm(self.gyro.axis)
            self.gyro.pos = 0.5 * self.l_shaft * a
            self.tip.pos = self.l_shaft * a
            t = t + delta_time * steps
