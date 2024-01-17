# coding:utf-8
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QHeaderView
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from Frontend.super.Ui_SuperadminAddAdmin import Ui_SuperadminAddAdmin


class SuperadminAddAdmin(Ui_SuperadminAddAdmin, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
