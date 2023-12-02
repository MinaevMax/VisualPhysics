from PySide6 import QtCore, QtWidgets
from i18n import t

import main
import screen
import widget


class ExperimentScreen(QtWidgets.QWidget):
    def __init__(self, window: QtWidgets.QMainWindow, branch: str, experiment: str):
        super().__init__(window)

        self.window = window
        self.branch = branch
        self.experiment = experiment

        try:
            if experiment not in main.branches[branch]['experiments']:
                raise ValueError

            app_bar = QtWidgets.QHBoxLayout()
            self._init_app_bar(app_bar)

            # Root layout
            layout = QtWidgets.QVBoxLayout(self)
            layout.addLayout(app_bar)
            layout.addStretch()
        except KeyError:
            heading = widget.HeadingWidget(t('screens.experiment.unknownBranchHeading').format(branch=branch))

            button = widget.ButtonWidget(t('back'))
            button.clicked.connect(self._open_experiments_screen)

            layout = QtWidgets.QVBoxLayout(self)
            layout.setSpacing(16)
            layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(heading)
            layout.addWidget(button)
        except ValueError:
            heading = widget.HeadingWidget(
                t('screens.experiment.unknownExperimentHeading').format(branch=branch, experiment=experiment))

            button = widget.ButtonWidget(t('back'))
            button.clicked.connect(self._open_experiments_screen)

            layout = QtWidgets.QVBoxLayout(self)
            layout.setSpacing(16)
            layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(heading)
            layout.addWidget(button)

        self.resize(1500, 605)
        window.move(window.pos().x() - (self.size().width() - window.size().width()) / 2, window.pos().y())
        window.setFixedSize(self.size())

    def _init_app_bar(self, layout: QtWidgets.QHBoxLayout):
        button = widget.ButtonWidget('←')
        button.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        button.setFixedHeight(24)
        button.clicked.connect(self._open_experiments_screen)

        heading = widget.HeadingWidget(t(f'experiments.{self.experiment}.name'))

        layout.setSpacing(16)
        layout.addWidget(button)
        layout.addWidget(heading)
        layout.addStretch()

    def _open_experiments_screen(self):
        self.window.setCentralWidget(screen.ExperimentsScreen(self.window, self.branch))
