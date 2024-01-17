# coding:utf-8
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QHeaderView, QMessageBox
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from Frontend.admin.Ui_AdminModifyBook import Ui_AdminModifyBook
from Backend.Lib_DB import Database


class AdminModifyBook(Ui_AdminModifyBook, QWidget):

    def __init__(self, parent=None, database=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.Lib_DB = database

        self.modifyButton.clicked.connect(self.modify_book)


    def modify_book(self):
        name = self.bookTitle.text()  # 获取书名
        index = self.bookIndex.text()  # 获取索引号
        author = self.bookAuthor.text()  # 获取作者
        pubdate = self.publishYear.text()  # 获取出版时间
        splitdate = pubdate.split('-')
        if len(name) == 0 or len(author) == 0 or len(pubdate) == 0:
            QMessageBox.warning(self, 'warning', '请补全图书信息！')
            return
        else:
            if not len(splitdate) == 3:
                QMessageBox.warning(self, 'warning', '出版时间格式错误！')
                return
            elif splitdate[0].isdigit() and splitdate[1].isdigit() and splitdate[2].isdigit():
                if int(splitdate[0]) in range(0, 2023) and int(splitdate[1]) in range(1, 13) and int(
                        splitdate[2]) in range(1, 32):
                    modified_book = {'id': index, 'name': name, 'author': author, 'pubdate': pubdate}
                    reply = QMessageBox.question(self,
                                                 '询问',
                                                 "确定要修改该图书吗？",
                                                 QMessageBox.Yes | QMessageBox.No,
                                                 QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        try:
                            self.Lib_DB.book_modify(modified_book)
                            self.bookAuthor.clear()
                            self.bookIndex.clear()
                            self.bookTitle.clear()
                            self.publishYear.clear()
                            QMessageBox.information(self, '通知', '修改图书成功！')
                        except Exception as e:
                            print(e)
                    else:
                        pass
