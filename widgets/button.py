from PySide6 import QtCore, QtGui, QtWidgets


class ButtonWidget(QtWidgets.QPushButton):
    border_color = '#eaeaea'
    background_color = '#fcfcfc'
    color = '#1b1b1b'

    def __init__(self, text: str):
        """Animation creation.

            Creating the button text, color and moving animation in case of interaction with the button.

            :param str text: The text of the button.

        """

        super().__init__(text)

        self._hover_background_animation = QtCore.QVariantAnimation()
        self._hover_background_animation.setStartValue(QtGui.QColor(self.background_color))
        self._hover_background_animation.setEndValue(QtGui.QColor('#f5f5f5'))
        self._hover_background_animation.valueChanged.connect(self.on_background_color_changed)
        self._hover_background_animation.setDuration(150)

        press_border_animation = QtCore.QVariantAnimation()
        press_border_animation.setStartValue(QtGui.QColor(self.border_color))
        press_border_animation.setEndValue(QtGui.QColor(f'{self.border_color}').setAlpha(0))
        press_border_animation.valueChanged.connect(self.on_border_color_changed)
        press_border_animation.setDuration(150)

        press_background_animation = QtCore.QVariantAnimation()
        press_background_animation.setStartValue(QtGui.QColor('#f5f5f5'))
        press_background_animation.setEndValue(QtGui.QColor('#ededed'))
        press_background_animation.valueChanged.connect(self.on_background_color_changed)
        press_background_animation.setDuration(150)

        press_color_animation = QtCore.QVariantAnimation()
        press_color_animation.setStartValue(QtGui.QColor(self.color))
        press_color_animation.setEndValue(QtGui.QColor('#5d5d5d'))
        press_color_animation.valueChanged.connect(self.on_color_changed)
        press_color_animation.setDuration(150)

        self._press_animation = QtCore.QParallelAnimationGroup()
        self._press_animation.addAnimation(press_border_animation)
        self._press_animation.addAnimation(press_background_animation)
        self._press_animation.addAnimation(press_color_animation)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self._update_style_sheet()

    def _update_style_sheet(self):
        """Change the button look.

            The function sets style sheet.

        """
        self.setStyleSheet(f"""
                QPushButton {{
                    height: 32px;
                    padding: 0 14px;
                    border: 1px solid {self.border_color};
                    border-radius: 6px;
                    background-color: {self.background_color};
                    color: {self.color};
                }}
            """)

    def on_border_color_changed(self, border_color: QtGui.QColor):
        """Change the button look.

            The function changes the button border color.

            :param QtGui.QColor border_color: the color of button border.

        """
        self.border_color = border_color.name()
        self._update_style_sheet()

    def on_background_color_changed(self, background_color: QtGui.QColor):
        """Change the button look.

            The function changes the button background color.

            :param QtGui.QColor background_color: the color of button background.

        """
        self.background_color = background_color.name()
        self._update_style_sheet()

    def on_color_changed(self, color: QtGui.QColor):
        """Change the button look.

            The function changes the button text color.

            :param QtGui.QColor color: the color of button text.

        """
        self.color = color.name()
        self._update_style_sheet()

    def enterEvent(self, event):
        """Event check.

            Enter event check.

            :param event: event.
        """
        self._hover_background_animation.setDirection(QtCore.QAbstractAnimation.Direction.Forward)
        self._hover_background_animation.start()

        super().enterEvent(event)

    def leaveEvent(self, event):
        """Event check.

            Leave event check.

            :param event: event.
        """
        self._hover_background_animation.setDirection(QtCore.QAbstractAnimation.Direction.Backward)
        self._hover_background_animation.start()

        super().leaveEvent(event)

    def mousePressEvent(self, event):
        """Event check.

            Press event check.

            :param event: event.
        """
        self._press_animation.setDirection(QtCore.QAbstractAnimation.Direction.Forward)
        self._press_animation.start()

        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """Event check.

            Release event check.

            :param event: event.
        """
        self._press_animation.setDirection(QtCore.QAbstractAnimation.Direction.Backward)
        self._press_animation.start()

        super().mouseReleaseEvent(event)
