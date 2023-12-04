from PySide6 import QtCore, QtWebEngineWidgets, QtWidgets
from i18n import t

import constants
import main
import screens
import widgets
from experiments import Experiment


class ExperimentScreen(QtWidgets.QWidget):
    experiment: Experiment | None = None

    def __init__(self, window: QtWidgets.QMainWindow, branch: str, experiment: str):
        """Creating the main experiment screen.

            Creating the experiment screen, using the name and branch of the experiment.

            :param QtWidgets.QMainWindow window: window canvas.
            :param branch str: the branch of the experiment.
            :param experiment str: the name of the experiment.
            :raise KeyError if there is no branch.
            :raise KeyError if there is no experiment.
        """
        super().__init__(window)

        self.window = window
        self.branch = branch
        self.experiment_name = experiment

        try:
            try:
                _ = main.branches[branch]
            except KeyError:
                heading = widgets.HeadingWidget(t('screens.experiment.unknownBranchHeading').format(branch=branch))

                button = widgets.ButtonWidget(t('back'))
                button.clicked.connect(self._open_home_screen)

                layout = QtWidgets.QVBoxLayout(self)
                layout.setSpacing(16)
                layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(heading)
                layout.addWidget(button)

                raise Exception

            try:
                _ = main.branches[branch]['experiments'][experiment]
            except KeyError:
                heading = widgets.HeadingWidget(
                    t('screens.experiment.unknownExperimentHeading').format(branch=branch, experiment=experiment))

                button = widgets.ButtonWidget(t('back'))
                button.clicked.connect(self._open_experiments_screen)

                layout = QtWidgets.QVBoxLayout(self)
                layout.setSpacing(16)
                layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(heading)
                layout.addWidget(button)

                raise Exception

            app_bar = QtWidgets.QHBoxLayout()
            self._init_app_bar(app_bar)

            content = QtWidgets.QHBoxLayout()

            if t(f'experiments.{self.experiment_name}.description') == '' \
                    and main.branches[branch]['experiments'][experiment] is None:
                subheading = widgets.HeadingWidget(
                    t('screens.experiment.noDetailsSubheading'),
                    widgets.heading.HeadingLevel.TWO,
                )
                subheading.setSizePolicy(
                    QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Expanding,
                    ),
                )
                subheading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                content.addWidget(subheading)
            else:
                self._init_content(content)

            # Root layout
            layout = QtWidgets.QVBoxLayout(self)
            layout.addLayout(app_bar)
            layout.addLayout(content)
        except Exception:
            pass

        self.resize(1408, constants.DEFAULT_WINDOW_HEIGHT)
        window.move(window.pos().x() - (self.size().width() - window.size().width()) / 2, window.pos().y())
        window.setFixedSize(self.size())

    def _init_app_bar(self, layout: QtWidgets.QHBoxLayout):
        """Creating experiment bar.

            Creating experiment bar, buttons and layout.

            :layout QtWidgets.QHBoxLayout: the base layout.
        """
        button = widgets.ButtonWidget('←')
        button.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        button.setFixedHeight(24)
        button.clicked.connect(self._open_experiments_screen)

        heading = widgets.HeadingWidget(t(f'experiments.{self.experiment_name}.name'))

        layout.setSpacing(16)
        layout.addWidget(button)
        layout.addWidget(heading)

    def _init_content(self, layout: QtWidgets.QHBoxLayout):
        """Creating widgets.

            Creating widgets for the experiment screen.

            :param layout QtWidgets.QHBoxLayout: experiment screen layout.
        """
        layout.setSpacing(16)

        if t(f'experiments.{self.experiment_name}.description') == '':
            subheading = widgets.HeadingWidget(
                t('screens.experiment.noDescriptionSubheading'),
                widgets.heading.HeadingLevel.TWO,
            )
            subheading.setMinimumWidth(512)
            subheading.setSizePolicy(QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Policy.Maximum,
                QtWidgets.QSizePolicy.Policy.Expanding,
            ))
            subheading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            layout.addWidget(subheading)
        else:
            description = QtWidgets.QLabel(t(f'experiments.{self.experiment_name}.description'))
            description.setMinimumWidth(512)
            description.setSizePolicy(QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Policy.Maximum,
                QtWidgets.QSizePolicy.Policy.Expanding,
            ))
            description.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
            description.setWordWrap(True)

            layout.addWidget(description)

        if main.branches[self.branch]['experiments'][self.experiment_name] is None:
            subheading = widgets.HeadingWidget(
                t('screens.experiment.noVisualisationSubheading'),
                widgets.heading.HeadingLevel.TWO,
            )
            subheading.setMaximumWidth(9999)
            subheading.setSizePolicy(
                QtWidgets.QSizePolicy(
                    QtWidgets.QSizePolicy.Policy.Maximum,
                    QtWidgets.QSizePolicy.Policy.Expanding,
                ),
            )
            subheading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            layout.addWidget(subheading)
        else:
            self.experiment = main.branches[self.branch]['experiments'][self.experiment_name]()
            self.experiment.start()

            browser = QtWebEngineWidgets.QWebEngineView()
            browser.setUrl('http://127.0.0.1:63794/')
            browser.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
            browser.setContentsMargins(9999, 0, 0, 0)
            browser.loadFinished.connect(
                lambda event: browser.setContentsMargins(0, 0, 0, 0) if event else browser.reload(),
            )

            layout.addWidget(browser)

    def _open_home_screen(self):
        """Opening the home screen.

            Opening the home screen.
        """
        if self.experiment is not None:
            self.experiment.terminate()

        self.window.setCentralWidget(screens.HomeScreen(self.window))

    def _open_experiments_screen(self):
        """Opening the experiments screen.

            Opening the experiments list screen.
        """
        if self.experiment is not None:
            self.experiment.terminate()

        self.window.setCentralWidget(screens.ExperimentsScreen(self.window, self.branch))
