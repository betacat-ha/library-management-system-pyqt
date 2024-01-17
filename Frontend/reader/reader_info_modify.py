# coding:utf-8
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QHeaderView
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from Frontend.reader.Ui_ReaderInfoModify import Ui_RederInfoModify


class ReaderInfoModify(Ui_RederInfoModify, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
