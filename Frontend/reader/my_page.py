# coding:utf-8
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon, Icon

from Frontend.reader.Ui_MyPage import Ui_MyPage


class MyPage(Ui_MyPage, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        # set the icon of button
        self.pinPersonButton.setIcon(FluentIcon.PIN)
        self.moreButton.setIcon(FluentIcon.MORE)
        self.pinBorrowButton.setIcon(FluentIcon.PIN)

        setFont(self.progressRing, 16)

        # add shadow effect to card
        self.setShadowEffect(self.BorrowInfoCard)
        self.setShadowEffect(self.personalInfoCard)

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)
