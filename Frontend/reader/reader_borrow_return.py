# coding:utf-8
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QAbstractItemView
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from Frontend.reader.Ui_ReaderBorrowReturn import Ui_ReaderBorrowReturn


class ReaderBorrowReturn(Ui_ReaderBorrowReturn, QWidget):

    def __init__(self, parent=None, database=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.bookList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.Lib_DB = database

    def refresh_rent_book_list(self, stu_id):
        results = self.Lib_DB.browse_rent(stu_id)
        self.bookList.clearContents()
        self.bookList.setRowCount(0)
        if not len(results) == 0:
            for line in results:
                searched_book = {'id': line[0], 'name': '', 'author': '', 'pubdate': ''}
                book = self.Lib_DB.search_book(searched_book)
                print(book)
                currentRowCount = self.bookList.rowCount()
                self.bookList.insertRow(currentRowCount)
                self.bookList.setItem(currentRowCount, 0, QTableWidgetItem(book[0][0]))
                self.bookList.setItem(currentRowCount, 1, QTableWidgetItem(book[0][2]))
                if str(book[0][3].strftime('%Y-%m-%d')).split("-", 1)[1] == '12-17':
                    self.bookList.setItem(currentRowCount, 2,
                                        QTableWidgetItem(
                                            str(book[0][3].strftime('%Y-%m-%d')).split("-")[
                                                0]))
                else:
                    self.bookList.setItem(currentRowCount, 2,
                                        QTableWidgetItem(
                                            str(book[0][3].strftime('%Y-%m-%d'))))
                self.bookList.setItem(currentRowCount, 3, QTableWidgetItem(str(book[0][1])))
                self.bookList.setEditTriggers(QAbstractItemView.NoEditTriggers)