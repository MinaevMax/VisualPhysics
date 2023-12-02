import functools

from PySide6 import QtCore, QtSvgWidgets, QtWidgets
from i18n import t

import constant
import main
import screen
import widget


class HomeScreen(QtWidgets.QWidget):
    def __init__(self, window: QtWidgets.QMainWindow):
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

        # Root layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(image_container)
        layout.addLayout(content_container)

        self.resize(constant.DEFAULT_WINDOW_WIDTH, constant.DEFAULT_WINDOW_HEIGHT)

        if window.size().width() > constant.DEFAULT_WINDOW_WIDTH:
            window.move(window.pos().x() + (window.size().width() - self.size().width()) / 2, window.pos().y())

        window.setFixedSize(self.size())

    def _init_headings(self, layout: QtWidgets.QVBoxLayout):
        layout.setSpacing(8)

        heading = widget.HeadingWidget(t('screens.home.heading'))
        heading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        subheading = widget.HeadingWidget(t('screens.home.subheading'), widget.heading.HeadingLevel.TWO)
        subheading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(heading)
        layout.addWidget(subheading)

    def _init_buttons(self, layout: QtWidgets.QHBoxLayout):
        left_container = QtWidgets.QVBoxLayout()
        right_container = QtWidgets.QVBoxLayout()

        for i, branch in enumerate(main.branches):
            button = widget.ButtonWidget(t(f'branches.{branch}'))
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
        self.window.setCentralWidget(screen.ExperimentsScreen(self.window, branch))
