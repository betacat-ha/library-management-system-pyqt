# coding:utf-8
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QHeaderView, QMessageBox
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon
from Backend.Lib_DB import Database

from Frontend.admin.Ui_AdminAddBook import Ui_AdminAddBook


class AdminAddBook(Ui_AdminAddBook, QWidget):

    def __init__(self, parent=None, database=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.Lib_DB = database
        self.addButton.clicked.connect(self.add_book)

    def add_book(self):
        name = self.bookTitle.text()  # 获取书名
        index = self.bookIndex.text()  # 获取索引号
        author = self.bookAuthor.text()  # 获取作者
        pubdate = self.publishYear.text()  # 获取出版时间
        splitdate = pubdate.split('-')

        if len(name) == 0 or len(index) == 0 or len(author) == 0 or len(pubdate) == 0:
            QMessageBox.warning(self, 'warning', '请补书籍信息！')
        else:
            if not index.isdigit():
                QMessageBox.warning(self, 'warning', '索引号格式错误！')
            elif not len(splitdate) == 3:
                QMessageBox.warning(self, 'warning', '出版时间格式错误！')
            elif splitdate[0].isdigit() and splitdate[1].isdigit() and splitdate[2].isdigit():
                if int(splitdate[0]) in range(0, 2023) and int(splitdate[1]) in range(1, 13) and int(
                        splitdate[2]) in range(1, 32):
                    new_book = {'id': index, 'name': name, 'author': author, 'pubdate': pubdate}
                    try:
                        self.Lib_DB.insert_book(new_book)
                        QMessageBox.information(self, '通知', '添加图书成功！')
                        self.bookAuthor.clear()
                        self.bookIndex.clear()
                        self.bookTitle.clear()
                        self.publishYear.clear()
                    except Exception as e:
                        print(e)
                        QMessageBox.warning(self, 'warning', '索引已存在！')
                else:
                    QMessageBox.warning(self, 'warning', '出版时间格式错误！')
            else:
                QMessageBox.warning(self, 'warning', '出版时间格式错误！')
