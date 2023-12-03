from enum import Enum

from PySide6 import QtWidgets


class HeadingLevel(Enum):
    """Heading

        Returnes the heading level.

        :example:

    #   >>> HL = HeadingLevel.ONE
    #   >>> level = ONE
    #   >>> HL == level
        True
    """
    ONE = 1
    TWO = 2


class HeadingWidget(QtWidgets.QLabel):
    """Heading

        Creates the heading(Label). The size if chosen by the level of the heading.

    """
    def __init__(self, text: str, level: HeadingLevel = HeadingLevel.ONE):
        super().__init__(text)

        font_size = 0

        match level:
            case HeadingLevel.ONE:
                font_size = 28
            case HeadingLevel.TWO:
                font_size = 20
            case _:
                TypeError('`level` must be one of HeadingLevel enum')

        self.setStyleSheet(f'''
            QLabel {{
                font-size: {font_size}px;
            }}
        ''')
