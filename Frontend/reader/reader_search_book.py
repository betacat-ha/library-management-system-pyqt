from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Frontend.reader.Ui_ReaderSearchBook import Ui_ReaderSearchBook
from Backend.Lib_DB import Database
import time


class ReaderSearchBook(QWidget, Ui_ReaderSearchBook):
    def __init__(self, parent=None, database:Database=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.bookList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.Lib_DB = database

        self.searchButton.clicked.connect(self.search_book)

    # 实现读者界面的书刊查找
    def search_book(self):
        name = self.bookTitle.text()  # 获取书名
        index = self.bookIndex.text()  # 获取索引号
        author = self.bookAuthor.text()  # 获取作者
        fardate = self.publishYearStart.text()
        neardate = self.publishYearEnd.text()
        timelen = 0.0
        splitdate1 = fardate.split('-')
        splitdate2 = neardate.split('-')

        if len(name) == 0 and len(index) == 0 and len(author) == 0 and (len(fardate) == 0 and len(neardate) == 0):
            self.search_all_book()
            return
        else:
            if not len(index) == 0:
                if not index.isdigit():
                    QMessageBox.warning(self, 'warning', '索引号格式错误！')
                    return
            if len(index) == 0:
                index = -1
            if (len(fardate) == 0 and not len(neardate) == 0) or (not len(fardate) == 0 and len(neardate) == 0):
                QMessageBox.warning(self, 'warning', '请补全出版时间范围！')
            if not len(fardate) == 0 and not len(neardate) == 0:
                if not len(splitdate1) == 3 or not len(splitdate2) == 3:
                    QMessageBox.warning(self, 'warning', '出版时间格式错误！')
                    return
                elif splitdate1[0].isdigit() and splitdate1[1].isdigit() and splitdate1[2].isdigit() and splitdate2[
                    0].isdigit() and splitdate2[1].isdigit() and splitdate2[2].isdigit():
                    if not int(splitdate1[0]) in range(0, 2023) or not int(splitdate1[1]) in range(1, 13) or not int(
                            splitdate1[2]) in range(1, 32) or not int(splitdate2[0]) in range(0, 2023) or not int(
                        splitdate2[1]) in range(1, 13) or not int(splitdate2[2]) in range(1, 32):
                        QMessageBox.warning(self, 'warning', '出版时间格式错误！')
                        return
                else:
                    QMessageBox.warning(self, 'warning', '出版时间格式错误！')
                    return
            try:
                searched_book = {'id': index, 'name': name, 'author': author, 'fardate': fardate, 'neardate': neardate}
                print(searched_book)
                st = time.time()
                results = self.Lib_DB.reader_search_book(searched_book)
                timelen = time.time() - st
                if len(results) == 0:
                    QMessageBox.warning(self, 'warning',
                                        '未查找到符合结果，请检查输入信息是否正确！查询用时：%4f s' % timelen)
                else:
                    QMessageBox.information(self, '通知',
                                            '查询完毕！查询用时：%4f s' % timelen)

                self.refresh_book_list(results)
            except Exception as e:
                QMessageBox.warning(self, 'warning',
                                    '未查找到符合结果，请检查输入信息是否正确！查询用时：%4f s' % timelen)
                print(e)

    def search_all_book(self):
        try:
            results = self.Lib_DB.show_book()
            self.refresh_book_list(results)
        except Exception as e:
            print('%s [ERROR] search_all_book:' % time.time())
            print(e)

    # 刷新书刊列表
    def refresh_book_list(self, book_list=None):
        self.bookList.clearContents()
        self.bookList.setRowCount(0)

        if book_list is None or len(book_list) == 0:
            return


        for line in book_list:
            currentRowCount = self.bookList.rowCount()
            self.bookList.insertRow(currentRowCount)
            self.bookList.setItem(currentRowCount, 0, QTableWidgetItem(line[0]))
            self.bookList.setItem(currentRowCount, 1, QTableWidgetItem(line[2]))
            if str(line[3].strftime('%Y-%m-%d')).split("-", 1)[1] == '12-17':
                self.bookList.setItem(currentRowCount, 2,
                                      QTableWidgetItem(
                                          str(line[3].strftime('%Y-%m-%d')).split("-")[
                                              0]))
            else:
                self.bookList.setItem(currentRowCount, 2,
                                      QTableWidgetItem(
                                          str(line[3].strftime('%Y-%m-%d'))))
            self.bookList.setItem(currentRowCount, 3,
                                  QTableWidgetItem(str(line[1])))
            self.bookList.setEditTriggers(QAbstractItemView.NoEditTriggers)
