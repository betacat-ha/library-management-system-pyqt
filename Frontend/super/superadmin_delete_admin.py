# coding:utf-8
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QHeaderView
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from Frontend.super.Ui_SuperadminDeleteAdmin import Ui_SuperadminDeleteAdmin


class SuperadminDeleteAdmin(Ui_SuperadminDeleteAdmin, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
