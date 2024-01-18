# coding:utf-8
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QHeaderView, QTableWidgetItem, QMessageBox, \
    QAbstractItemView
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from Frontend.super.Ui_SuperSearch import Ui_SuperSearch


class SuperadminSearch(Ui_SuperSearch, QWidget):

    def __init__(self, parent=None, database=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.adminList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.Lib_DB = database

        self.adminSearchEdit.searchSignal.connect(self.find_admin)

    # 实现查找管理员
    def find_admin(self):
        id = self.adminSearchEdit.text()
        if len(id) == 0:
            try:
                admins = self.Lib_DB.show_admin()
                print(admins)
                if not len(admins) == 0:
                        self.refresh_admin_list(admins)
                else:
                    QMessageBox.warning(self.Super, '警告', '暂无管理员信息！')
            except Exception as e:
                print(e)

        elif not id.isdigit():
            QMessageBox.warning(self.Super, '警告', '管理员工号格式错误！')
            return
        else:
            try:
                results = self.Lib_DB.search_admin(id)
                if len(results) == 0:
                    QMessageBox.warning(self.Super, '警告', '未找到管理员，请检查工号是否正确！')
                    return
                else:
                    self.refresh_admin_list(results)
            except Exception as e:
                print(e)



    def refresh_admin_list(self, admin_list):
        self.adminList.clearContents()
        self.adminList.setRowCount(0)

        for line in admin_list:
            currentRowCount = self.adminList.rowCount()
            self.adminList.insertRow(currentRowCount)
            self.adminList.setItem(currentRowCount, 0, QTableWidgetItem(str(line['admin_id'])))
            self.adminList.setItem(currentRowCount, 1, QTableWidgetItem(line['admin_user']))
            self.adminList.setItem(currentRowCount, 2, QTableWidgetItem(line['admin_password']))
            self.adminList.setEditTriggers(QAbstractItemView.NoEditTriggers)