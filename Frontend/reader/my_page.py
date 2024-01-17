# coding:utf-8
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from Frontend.reader.Ui_MyPage import Ui_MyPage


class MyPage(Ui_MyPage, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
