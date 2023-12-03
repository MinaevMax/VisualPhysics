import functools

from PySide6 import QtCore, QtSvgWidgets, QtWidgets
from i18n import t

import constants
import main
import screens
import widgets


class ExperimentsScreen(QtWidgets.QWidget):
    def __init__(self, window: QtWidgets.QMainWindow, branch: str):
        super().__init__(window)

        self.window = window
        self.branch = branch

        # Image
        image = QtSvgWidgets.QSvgWidget('assets/images/teaching.svg')
        image.setFixedSize(450, 332)

        image_container = QtWidgets.QVBoxLayout()
        image_container.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        image_container.addStretch()
        image_container.addWidget(image)
        image_container.addStretch()

        # Content
        headings_container = QtWidgets.QVBoxLayout()
        self._init_headings(headings_container)

        buttons_container = QtWidgets.QVBoxLayout()
        self._init_buttons(buttons_container)

        content_container = QtWidgets.QVBoxLayout()
        content_container.setSpacing(20)
        content_container.addLayout(headings_container)
        content_container.addLayout(buttons_container)

        # Root layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(image_container)
        layout.addLayout(content_container)

        self.resize(constants.DEFAULT_WINDOW_WIDTH, constants.DEFAULT_WINDOW_HEIGHT)

        if window.size().width() != constants.DEFAULT_WINDOW_WIDTH:
            window.move(window.pos().x() + (window.size().width() - self.size().width()) / 2, window.pos().y())

        window.setFixedSize(self.size())

    def _init_headings(self, layout: QtWidgets.QVBoxLayout):
        try:
            _ = main.branches[self.branch]

            heading = widgets.HeadingWidget(t('screens.experiments.heading'))
            heading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(heading)
        except KeyError:
            heading = widgets.HeadingWidget(t('screens.experiments.unknownBranchSubheading').format(branch=self.branch))
            heading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(heading)

    def _init_buttons(self, layout: QtWidgets.QVBoxLayout):
        branches_buttons = QtWidgets.QHBoxLayout()
        left_container = QtWidgets.QVBoxLayout()
        right_container = QtWidgets.QVBoxLayout()

        try:
            for i, experiment in enumerate(main.branches[self.branch]['experiments']):
                button = widgets.ButtonWidget(t(f'experiments.{experiment}.name'))
                button.clicked.connect(functools.partial(self._open_experiment_screen, experiment))

                if i % 2 == 0:
                    left_container.addWidget(button)
                else:
                    right_container.addWidget(button)
        except KeyError:
            pass

        branches_buttons.setSpacing(4)
        layout.setSpacing(4)
        left_container.setSpacing(4)
        left_container.setSpacing(4)

        back_button = widgets.ButtonWidget(t('back'))
        back_button.clicked.connect(self._open_home_screen)

        branches_buttons.addLayout(left_container)
        branches_buttons.addLayout(right_container)
        layout.addLayout(branches_buttons)
        layout.addWidget(back_button)

    def _open_home_screen(self):
        self.window.setCentralWidget(screens.HomeScreen(self.window))

    def _open_experiment_screen(self, experiment: str):
        self.window.setCentralWidget(screens.ExperimentScreen(self.window, self.branch, experiment))
