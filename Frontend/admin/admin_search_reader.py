# coding:utf-8
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QHeaderView, QTableWidgetItem, QAbstractItemView, \
    QMessageBox
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon
from Backend.Lib_DB import Database
from Frontend.admin.Ui_AdminSearchReader import Ui_AdminSearchReader


class AdminSearchReader(Ui_AdminSearchReader, QWidget):

    def __init__(self, parent=None, database=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.Lib_DB = database
        self.browse_reader()
        self.readerList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def browse_reader(self):
        readers = self.Lib_DB.show_reader()
        print(readers)
        if not len(readers) == 0:
            try:
                self.totalreader = 0
                self.readerList.clearContents()
                self.readerList.setRowCount(0)
                currentRowCount = 0
                for line in readers:
                    currentRowCount = self.readerList.rowCount()
                    self.readerList.insertRow(currentRowCount)
                    self.readerList.setItem(currentRowCount, 0, QTableWidgetItem(line['stu_user']))
                    self.readerList.setItem(currentRowCount, 1, QTableWidgetItem(str(line['stu_password'])))
                    self.readerList.setItem(currentRowCount, 2, QTableWidgetItem(line['stu_name']))
                    self.readerList.setItem(currentRowCount, 3, QTableWidgetItem(str(line['stu_id'])))
                    self.readerList.setItem(currentRowCount, 4, QTableWidgetItem(line['stu_dep']))
                    self.readerList.setEditTriggers(QAbstractItemView.NoEditTriggers)
                print("浏览读者成功")
                self.totalreader = currentRowCount + 1
                # self.lineEdit_8.setText(str(self.totalreader))
            except Exception as e:
                print(e)
        else:
            QMessageBox.warning(self, '警告', '暂无读者信息！')