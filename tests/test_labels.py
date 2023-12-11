from PySide6.QtGui import QColor
from PySide6.QtWidgets import QLabel
from pytestqt.qt_compat import qt_api
from pytestqt.qtbot import QtBot

from widgets.heading import HeadingWidget, HeadingLevel


def test_default_text(qtbot: QtBot):
    heading = HeadingWidget('Text')

    assert heading.text() == 'Text'


def test_default_text_size_large(qtbot: QtBot):
    heading = HeadingWidget('Text', level=HeadingLevel.ONE)

    assert heading.font_size == 28


def test_default_text_size_small(qtbot: QtBot):
    heading = HeadingWidget('Text', level=HeadingLevel.TWO)

    assert heading.font_size == 20