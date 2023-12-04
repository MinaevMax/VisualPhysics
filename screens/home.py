import functools

from PySide6 import QtCore, QtSvgWidgets, QtWebEngineWidgets, QtWidgets
from i18n import t

import constants
import main
import screens
import widgets


class HomeScreen(QtWidgets.QWidget):
    def __init__(self, window: QtWidgets.QMainWindow):
        """Creating home screen.

            Creating the home screen, using the name of branches.

            :param QtWidgets.QMainWindow window: window canvas.
        """
        super().__init__(window)

        self.window = window

        # Image
        image = QtSvgWidgets.QSvgWidget('assets/images/geniuses.svg')
        image.setFixedSize(450, 257)

        image_container = QtWidgets.QVBoxLayout()
        image_container.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        image_container.addStretch()
        image_container.addWidget(image)
        image_container.addStretch()

        # Content
        headings_container = QtWidgets.QVBoxLayout()
        self._init_headings(headings_container)

        buttons_container = QtWidgets.QHBoxLayout()
        self._init_buttons(buttons_container)

        content_container = QtWidgets.QVBoxLayout()
        content_container.setSpacing(20)
        content_container.addLayout(headings_container)
        content_container.addLayout(buttons_container)

        # Some crazy stuff
        # WebEngineView is needed to initialize window for working with browser
        browser = QtWebEngineWidgets.QWebEngineView()
        browser.setHtml('')
        browser.hide()

        # Root layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(image_container)
        layout.addLayout(content_container)
        layout.addWidget(browser)

        self.resize(constants.DEFAULT_WINDOW_WIDTH, constants.DEFAULT_WINDOW_HEIGHT)

        if window.size().width() > constants.DEFAULT_WINDOW_WIDTH:
            window.move(window.pos().x() + (window.size().width() - self.size().width()) / 2, window.pos().y())

        window.setFixedSize(self.size())

    @staticmethod
    def _init_headings(layout: QtWidgets.QVBoxLayout):
        """Creating widgets.

            Сreating label for home screen.

            :param layout QtWidgets.QHBoxLayout: home screen layout.
        """
        layout.setSpacing(8)

        heading = widgets.HeadingWidget(t('screens.home.heading'))
        heading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        subheading = widgets.HeadingWidget(t('screens.home.subheading'), widgets.heading.HeadingLevel.TWO)
        subheading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(heading)
        layout.addWidget(subheading)

    def _init_buttons(self, layout: QtWidgets.QHBoxLayout):
        """Creating widgets.

            Creating widgets for home screen.

            :param layout QtWidgets.QHBoxLayout: home screen layout.
        """
        left_container = QtWidgets.QVBoxLayout()
        right_container = QtWidgets.QVBoxLayout()

        for i, branch in enumerate(main.branches):
            button = widgets.ButtonWidget(t(f'branches.{branch}'))
            button.clicked.connect(functools.partial(self.open_experiments_screen, branch))

            if i % 2 == 0:
                left_container.addWidget(button)
            else:
                right_container.addWidget(button)

        layout.setSpacing(4)
        left_container.setSpacing(4)
        left_container.setSpacing(4)

        layout.addLayout(left_container)
        layout.addLayout(right_container)

    def open_experiments_screen(self, branch: str):
        """Opening the experiments screen.

            Opening the experiments list screen.
        """
        self.window.setCentralWidget(screens.ExperimentsScreen(self.window, branch))
