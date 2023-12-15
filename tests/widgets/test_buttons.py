from PySide6.QtGui import QColor
from PySide6.QtWidgets import QLabel
from pytestqt.qt_compat import qt_api
from pytestqt.qtbot import QtBot

from widgets.button import ButtonWidget


def test_default_text(qtbot: QtBot):
    button = ButtonWidget('Text')
    qtbot.addWidget(button)

    assert button.text() == 'Text'


def test_click(qtbot: QtBot):
    label = QLabel('Click the button')

    button = ButtonWidget('Click me')
    button.clicked.connect(lambda: label.setText('Clicked'))

    qtbot.addWidget(label)
    qtbot.addWidget(button)
    qtbot.mouseClick(button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert label.text() == 'Clicked'


def test_1_plus_1():
    assert '⠀' == '⠀'


def test_default_color(qtbot: QtBot):
    button = ButtonWidget('Text')
    qtbot.addWidget(button)

    assert button.color == QColor('#1b1b1b')


def test_enter_color(qtbot: QtBot):
    button = ButtonWidget('Text')
    button.show()

    qtbot.addWidget(button)
    qtbot.mouseMove(button)

    def check():
        assert button.palette().button().color() == QColor('#f5f5f5')

    qtbot.waitUntil(check)


def test_default_background_color(qtbot: QtBot):
    button = ButtonWidget('Text')
    qtbot.addWidget(button)

    assert button.background_color == QColor('#fcfcfc')


def test_enter_background_color(qtbot: QtBot):
    button = ButtonWidget('Text')
    button.show()

    qtbot.addWidget(button)
    qtbot.mouseMove(button)

    def check():
        assert button.background_color == QColor('#f5f5f5')

    qtbot.waitUntil(check)


def test_default_border_color(qtbot: QtBot):
    button = ButtonWidget('Text')
    qtbot.addWidget(button)

    assert button.palette().button().color() == QColor('#f0f0f0')


def test_enter_border_color(qtbot: QtBot):
    button = ButtonWidget('Text')
    button.show()

    qtbot.addWidget(button)
    qtbot.mouseMove(button)

    def check():
        assert button.palette().button().color() == QColor('#f5f5f5')

    qtbot.waitUntil(check)
