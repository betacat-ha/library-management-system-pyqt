from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Frontend.reader.Ui_ReaderSearchBook import Ui_ReaderSearchBook


class ReaderSearchBook(QWidget, Ui_ReaderSearchBook):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.bookList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)