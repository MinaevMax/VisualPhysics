import locale
import sys

import i18n
from PySide6 import QtGui, QtWidgets

import constant
import screen.home

branches = {
    'mechanics': {
        'experiments': [
            'oscillation', 'gyroscope', 'elastic_collision', 'inelastic_collision', 'sliding_friction', 'gravitation',
        ],
    },
    'optics': {
        'experiments': [
            'diffraction', 'interference', 'point_light_source', 'real_light_source', 'reflection', 'refraction',
        ],
    },
    'electromagnetism': {
        'experiments': [
            'pull', 'repulsion', 'static_electricity', 'electricity', 'circuit_overload', 'electrical_short',
        ],
    },
    'thermodynamics': {
        'experiments': [
            'convection', 'thermal_conductivity', 'expansion', 'thermal_transition', 'thermal_radiation',
            'heat_exchange',
        ],
    },
}

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

    window = QtWidgets.QMainWindow()
    palette = window.palette()

    palette.setColor(window.backgroundRole(), 0xf3f3f3)

    window.resize(constant.DEFAULT_WINDOW_WIDTH, constant.DEFAULT_WINDOW_HEIGHT)
    window.setWindowIcon(QtGui.QIcon('assets/images/phantoms.png'))
    window.setCentralWidget(screen.HomeScreen(window))
    window.setPalette(palette)
    window.setStyleSheet("""
        * {
            font-family: 'Nunito Light', sans-serif;
            font-size: 14px;
            color: #1b1b1b;
        }
    """)
    window.show()

    sys.exit(app.exec())
