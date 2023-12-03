import locale
import os
import sys

import i18n
from PySide6 import QtGui, QtWidgets

import constants
import screens.home
from experiments import OscillationExperiment, GravitationExperiment, GyroscopeExperiment, PullExperiment, \
    CircuitOverloadExperiment, ThermalRadiationExperiment, HeatExchangeExperiment, DiffractionExperiment, \
    InterferenceExperiment, ThermalTransitionExperiment, ThermalConductivityExperiment, StaticElectricityExperiment, \
    SlidingFrictionExperiment, RepulsionExperiment, RefractionExperiment, ConvectionExperiment, ReflectionExperiment, \
    RealLightSourceExperiment, PointLightSourceExperiment, InelasticCollisionExperiment, ExpansionExperiment, \
    ElectricityExperiment, ElectricalShortExperiment, ElasticCollisionExperiment

branches = {
    'mechanics': {
        'experiments': {
            'oscillation': OscillationExperiment,
            'gyroscope': GyroscopeExperiment,
            'elastic_collision': ElasticCollisionExperiment,
            'inelastic_collision': InelasticCollisionExperiment,
            'sliding_friction': SlidingFrictionExperiment,
            'gravitation': GravitationExperiment,
        },
    },
    'optics': {
        'experiments': {
            'diffraction': DiffractionExperiment,
            'interference': InterferenceExperiment,
            'point_light_source': PointLightSourceExperiment,
            'real_light_source': RealLightSourceExperiment,
            'reflection': ReflectionExperiment,
            'refraction': RefractionExperiment,
        },
    },
    'electromagnetism': {
        'experiments': {
            'pull': PullExperiment,
            'repulsion': RepulsionExperiment,
            'static_electricity': StaticElectricityExperiment,
            'electricity': ElectricityExperiment,
            'circuit_overload': CircuitOverloadExperiment,
            'electrical_short': ElectricalShortExperiment,
        },
    },
    'thermodynamics': {
        'experiments': {
            'convection': ConvectionExperiment,
            'thermal_conductivity': ThermalConductivityExperiment,
            'expansion': ExpansionExperiment,
            'thermal_transition': ThermalTransitionExperiment,
            'thermal_radiation': ThermalRadiationExperiment,
            'heat_exchange': HeatExchangeExperiment,
        },
    },
}


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        palette = self.palette()
        palette.setColor(self.backgroundRole(), 0xf3f3f3)

        self.resize(constants.DEFAULT_WINDOW_WIDTH, constants.DEFAULT_WINDOW_HEIGHT)
        self.setWindowIcon(QtGui.QIcon('assets/images/phantoms.png'))
        self.setPalette(palette)
        self.setStyleSheet("""
                * {
                    font-family: 'Nunito Light', sans-serif;
                    font-size: 14px;
                    color: #1b1b1b;
                }
            """)

    def closeEvent(self, event: QtGui.QCloseEvent):
        os._exit(0)


if __name__ == '__main__':
    match locale.getlocale()[0]:
        case locale if 'ru' in locale.lower():
            i18n.set('locale', 'ru')
        case _:
            i18n.set('locale', 'en')

    i18n.resource_loader.init_json_loader()
    i18n.set('filename_format', '{locale}.{format}')
    i18n.set('file_format', 'json')
    i18n.set('skip_locale_root_data', True)
    i18n.set('enable_memoization', True)
    i18n.load_path.append('assets/locales/')

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('VisualPhysics')
    app.setApplicationVersion('0.0.1')

    QtGui.QFontDatabase.addApplicationFont('assets/fonts/nunito.ttf')

    window = Window()
    window.setCentralWidget(screens.HomeScreen(window))
    window.show()

    sys.exit(app.exec())
