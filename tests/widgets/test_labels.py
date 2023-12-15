from pytestqt.qtbot import QtBot

from widgets.heading import HeadingWidget, HeadingLevel


def test_default_text(qtbot: QtBot):
    heading = HeadingWidget('Text')
    qtbot.addWidget(heading)

    assert heading.text() == 'Text'


def test_default_text_size_large(qtbot: QtBot):
    heading = HeadingWidget('Text', level=HeadingLevel.ONE)
    qtbot.addWidget(heading)

    assert heading.font_size == 28


def test_default_text_size_small(qtbot: QtBot):
    heading = HeadingWidget('Text', level=HeadingLevel.TWO)
    qtbot.addWidget(heading)

    assert heading.font_size == 20
