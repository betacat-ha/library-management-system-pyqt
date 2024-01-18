import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Frontend.super.superadmin_add_admin import SuperadminAddAdmin
from Frontend.super.superadmin_delete_admin import SuperadminDeleteAdmin
from Frontend.super.superadmin_search import SuperadminSearch
from Frontend.reader.my_page import MyPage
from Frontend.reader.reader_search_book import ReaderSearchBook
from Frontend.reader.reader_borrow_return import ReaderBorrowReturn
from Frontend.reader.reader_info_modify import ReaderInfoModify
from Frontend.LoginAdmin import Ui_LoginAdmin
from Frontend.LoginReader import Ui_LoginReader
from Frontend.LoginSuper import Ui_LoginSuper
from Frontend.admin.admin_search_reader import AdminSearchReader
from Frontend.admin.admin_add_book import AdminAddBook
from Frontend.admin.admin_modify_book import AdminModifyBook
from Frontend.MainWin import Ui_MainWin
from Frontend.Register import Ui_Register
from Backend.Lib_DB import Database
from qframelesswindow import FramelessWindow, StandardTitleBar
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme,
                            NavigationAvatarWidget, SplitFluentWindow, FluentTranslator)
from qfluentwidgets import FluentIcon
import time

SuperUser = 'Super'  # 超级管理员用户名
SuperPassword = '123'  # 超级管理员密码


# 读者界面
class ReaderIn(SplitFluentWindow):
    def __init__(self, database=None):
        super().__init__()

        self.readerSearchBook = ReaderSearchBook(self, database)
        self.readerBorrowReturn = ReaderBorrowReturn(self, database)
        self.readerInfoModify = ReaderInfoModify(self)
        self.myPage = MyPage(self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        # add sub interface
        self.addSubInterface(self.myPage, FluentIcon.HOME, '主页')
        self.addSubInterface(self.readerSearchBook, FluentIcon.SEARCH, '书刊查找')
        self.addSubInterface(self.readerBorrowReturn, FluentIcon.LIBRARY, '借书/还书')
        self.addSubInterface(self.readerInfoModify, FluentIcon.SETTING, '个人信息修改')

        self.navigationInterface.addItem(
            routeKey='settingInterface',
            icon=FluentIcon.POWER_BUTTON,
            text='退出登录',
            position=NavigationItemPosition.BOTTOM,
            onClick=self.close
        )

    def initWindow(self):
        self.setWindowTitle('读者界面')
        self.setWindowIcon(QIcon(':/images/logo.png'))

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.resize((int)(w * 0.8), (int)(h * 0.9))
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


# 超管界面
class SupAD(SplitFluentWindow):
    def __init__(self, database=None):
        super().__init__()

        self.superadminAddAdmin = SuperadminAddAdmin(self)
        self.superadminDeleteAdmin = SuperadminDeleteAdmin(self)
        self.superadminSearch = SuperadminSearch(self, database)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        # add sub interface
        self.addSubInterface(self.superadminAddAdmin, FluentIcon.ADD, '增加管理员')
        self.addSubInterface(self.superadminDeleteAdmin, FluentIcon.DELETE, '删除管理员')
        self.addSubInterface(self.superadminSearch, FluentIcon.SEARCH, '管理员查询')

        self.navigationInterface.addItem(
            routeKey='settingInterface',
            icon=FluentIcon.POWER_BUTTON,
            text='退出登录',
            position=NavigationItemPosition.BOTTOM,
            onClick=self.close
        )

    def initWindow(self):
        self.setWindowTitle('超级管理员界面')
        self.setWindowIcon(QIcon(':/images/logo.png'))

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.resize((int)(w * 0.8), (int)(h * 0.9))
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)\


# 管理员界面
class AdminGUI(SplitFluentWindow):
    def __init__(self, database=None):
        super().__init__()

        self.adminSearchReader = AdminSearchReader(self, database)
        self.adminAddBook = AdminAddBook(self, database)
        self.adminModifyBook = AdminModifyBook(self, database)
        self.readerSearchBook = ReaderSearchBook(self, database)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        # add sub interface
        self.addSubInterface(self.readerSearchBook, FluentIcon.SEARCH, '书刊查找')
        self.addSubInterface(self.adminAddBook, FluentIcon.ADD, '添加图书')
        self.addSubInterface(self.adminModifyBook, FluentIcon.EDIT, '修改图书信息')
        self.addSubInterface(self.adminSearchReader, FluentIcon.PEOPLE, '查看读者信息')


        self.navigationInterface.addItem(
            routeKey='settingInterface',
            icon=FluentIcon.POWER_BUTTON,
            text='退出登录',
            position=NavigationItemPosition.BOTTOM,
            onClick=self.close
        )

    def initWindow(self):
        self.setWindowTitle('管理员界面')
        self.setWindowIcon(QIcon(':/images/logo.png'))

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.resize((int)(w * 0.8), (int)(h * 0.9))
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


# 主界面
class MainWin(FramelessWindow, Ui_MainWin):  # 实现前后端功能对接
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        self.setupUi(self)

        # 设置标题栏
        self.setTitleBar(StandardTitleBar(self))

        self.pushButton_7.clicked.connect(self.displayReader)  # 选择登录读者
        self.pushButton_6.clicked.connect(self.displayAdmin)
        self.pushButton_5.clicked.connect(self.displaySuper)
        self.pushButton_4.clicked.connect(self.close)
        self.Lib_DB = Database()
        self.Admin = AdminGUI(self.Lib_DB)
        self.LoginAdmin = LoginAdmin()
        self.LoginReader = LoginReader()
        self.LoginSuper = LoginSuper()
        self.Super = SupAD(self.Lib_DB)
        self.Reader = ReaderIn(self.Lib_DB)
        self.Register = Register()
        self.LoginAdmin.pushButton.clicked.connect(self.EnterAdmin)
        self.LoginSuper.pushButton.clicked.connect(self.EnterSuper)
        self.LoginReader.pushButton.clicked.connect(self.EnterReader)
        # self.Admin.Confirm_6.clicked.connect(self.delete_book)
        self.Super.superadminAddAdmin.finshButton.clicked.connect(self.add_admin)
        self.Super.superadminDeleteAdmin.finshButton.clicked.connect(self.delete_admin)
        self.Register.pushButton.clicked.connect(self.add_reader)
        self.Reader.readerInfoModify.confirm.clicked.connect(self.modify_reader)
        self.Reader.readerBorrowReturn.borrowButton.clicked.connect(self.borrow_book)
        self.Reader.readerBorrowReturn.returnButton.clicked.connect(self.return_book)
        self.CurrentReader = -1

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


    def displayRentBorrow(self):
        sender = self.Reader.sender()
        if sender.text() == "借书/还书":
            if not self.CurrentReader == -1:
                stu_id = self.CurrentReader
                try:
                    results = self.Lib_DB.browse_rent(stu_id)
                    self.Reader.tableWidget_2.clearContents()
                    self.Reader.tableWidget_2.setRowCount(0)
                    if not len(results) == 0:
                        for line in results:
                            searched_book = {'id': line[0], 'name': '', 'author': '', 'pubdate': ''}
                            book = self.Lib_DB.search_book(searched_book)
                            print(book)
                            currentRowCount = self.Reader.tableWidget_2.rowCount()
                            self.Reader.tableWidget_2.insertRow(currentRowCount)
                            self.Reader.tableWidget_2.setItem(currentRowCount, 0, QTableWidgetItem(book[0][0]))
                            self.Reader.tableWidget_2.setItem(currentRowCount, 1, QTableWidgetItem(book[0][2]))
                            if str(book[0][3].strftime('%Y-%m-%d')).split("-", 1)[1] == '12-17':
                                self.Reader.tableWidget_2.setItem(currentRowCount, 2,
                                                                  QTableWidgetItem(
                                                                      str(book[0][3].strftime('%Y-%m-%d')).split("-")[
                                                                          0]))
                            else:
                                self.Reader.tableWidget_2.setItem(currentRowCount, 2,
                                                                  QTableWidgetItem(
                                                                      str(book[0][3].strftime('%Y-%m-%d'))))
                            self.Reader.tableWidget_2.setItem(currentRowCount, 3, QTableWidgetItem(str(book[0][1])))
                            self.Reader.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
                except Exception as e:
                    print(e)
            else:
                print("CurrentReader为-1")
            self.Reader.stackedWidget.setCurrentIndex(2)

    def displayReader(self):
        self.LoginReader.show()

    def displayAdmin(self):
        self.LoginAdmin.show()

    def displaySuper(self):
        self.LoginSuper.show()

    def EnterAdmin(self):

        userName = self.LoginAdmin.lineEdit.text()  # 获取工号
        password = self.LoginAdmin.lineEdit_2.text()  # 获取密码
        if len(userName) == 0 or len(password) == 0:
            QMessageBox.warning(self.LoginAdmin, 'warning', '请补全工号或密码！')
        else:
            verify = self.Lib_DB.login_admin(userName, password)
            if verify:
                self.LoginAdmin.lineEdit.clear()
                self.LoginAdmin.lineEdit_2.clear()
                self.Admin.show()
                self.Admin.readerSearchBook.search_all_book()
                self.LoginAdmin.close()
            else:
                QMessageBox.warning(self.LoginAdmin, 'warning', '工号或密码错误，请检查！')

    def EnterSuper(self):

        userName = self.LoginSuper.lineEdit.text()  # 获取用户名
        password = self.LoginSuper.lineEdit_2.text()  # 获取密码
        if len(userName) == 0 or len(password) == 0:
            QMessageBox.warning(self.LoginSuper, 'warning', '请补全用户名或密码！')
        elif userName == SuperUser and password == SuperPassword:
            self.Super.show()
            self.Super.superadminSearch.find_admin()
            self.LoginSuper.close()
        else:
            QMessageBox.warning(self.LoginSuper, 'warning', '未找到该管理员！')

    def EnterReader(self):
        self.CurrentReader = -1
        userName = self.LoginReader.lineEdit.text()  # 获取学号
        password = self.LoginReader.lineEdit_4.text()  # 获取密码
        if len(userName) == 0 or len(password) == 0:
            QMessageBox.warning(self.LoginReader, 'warning', '请补全学号或密码！')
        else:
            verify = self.Lib_DB.login_reader(userName, password)
            if verify:
                self.LoginReader.lineEdit.clear()
                self.LoginReader.lineEdit_4.clear()

                self.CurrentReader = userName
                self.Reader.show()
                self.Reader.readerBorrowReturn.refresh_rent_book_list(self.CurrentReader)
                self.Reader.readerSearchBook.search_all_book()
                self.LoginReader.close()
            else:
                QMessageBox.warning(self.LoginReader, 'warning', '学号或密码错误！')

    def displayRegister(self, type):
        self.Register.show()

    # 实现读者信息修改
    def modify_reader(self):
        ui = self.Reader.readerInfoModify
        name = ui.name.text()
        id = ui.id.text()
        dep = ui.dep.text()
        oldpassword = ui.oldPassword.text()
        newpassword = ui.newPassword.text()
        if len(name) == 0 or len(id) == 0 or len(dep) == 0 or len(oldpassword) == 0 or len(newpassword) == 0:
            QMessageBox.warning(self.Reader, 'warning', '请补全读者信息！')
        elif not id.isdigit():
            QMessageBox.warning(self.Reader, 'warning', '学号格式错误！')
        else:
            reader = {'id': id, 'name': name, 'dep': dep, 'oldpassword': oldpassword, 'newpassword': newpassword}
            try:
                verify = self.Lib_DB.reader_modify(reader)
                if verify:
                    QMessageBox.information(self.Admin, '通知', '修改读者成功！')
                    # ui.name.clear()
                    # ui.id.clear()
                    # ui.dep.clear()
                    ui.oldPassword.clear()
                    ui.newPassword.clear()

                else:
                    QMessageBox.warning(self.Reader, '错误', '请检查学号和原密码是否正确！')
            except Exception as e:
                print(e)

    def delete_book(self):
        index = self.Admin.User_9.text()
        print(index)
        reply = QMessageBox.question(self.Admin,
                                     '询问',
                                     "确定要删除该图书吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                self.Lib_DB.book_delete(index)
                self.Admin.lineEdit.clear()
                self.Admin.lineEdit_2.clear()
                self.Admin.lineEdit_3.clear()
                self.Admin.lineEdit_4.clear()
                self.Admin.User_9.clear()
                QMessageBox.information(self.Admin, '通知', '删除图书成功！')
                self.Admin.stackedWidget.setCurrentIndex(0)
            except Exception as e:
                print(e)
        else:
            pass

    # 实现添加管理员
    def add_admin(self):
        ui = self.Super.superadminAddAdmin
        user = ui.adminName.text()
        id = ui.adminId.text()
        password = ui.adminPassword.text()
        if len(user) == 0 or len(id) == 0 or len(password) == 0:
            QMessageBox.warning(self.Super, '警告', '请补全管理员信息！')
            return
        elif not id.isdigit():
            QMessageBox.warning(self.Super, '警告', '管理员工号格式错误！')
            return
        else:
            admin = {'id': id, 'user': user, 'password': password}
            try:
                self.Lib_DB.insert_admin(admin)
                QMessageBox.information(self.Super, '通知', '添加管理员成功！')
                ui.adminId.clear()
                ui.adminName.clear()
                ui.adminPassword.clear()
            except Exception as e:
                print(e)

    # 实现删除管理员
    def delete_admin(self):
        ui = self.Super.superadminDeleteAdmin
        id = ui.adminId.text()
        if len(id) == 0:
            QMessageBox.warning(self.Super, '警告', '请补全工号！')
            return
        elif not id.isdigit():
            QMessageBox.warning(self.Super, '警告', '管理员工号格式错误！')
            return
        else:
            results = self.Lib_DB.search_admin(id)
            if len(results) == 0:
                QMessageBox.warning(self.Super, '警告', '未找到管理员，请检查工号是否正确！')
                return
            else:
                reply = QMessageBox.question(self.Super,
                                             '询问',
                                             "确定要删除该管理员吗？",
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    try:
                        self.Lib_DB.admin_delete(id)
                        ui.adminId.clear()
                        QMessageBox.information(self.Super, '通知', '删除管理员成功！')
                    except Exception as e:
                        print(e)
                else:
                    pass

    # 实现读者注册（添加读者）
    def add_reader(self):
        user = self.Register.lineEdit_4.text()
        password = self.Register.lineEdit_2.text()
        name = self.Register.lineEdit_5.text()
        dep = self.Register.lineEdit_6.text()
        id = self.Register.lineEdit_7.text()
        if len(user) == 0 or len(id) == 0 or len(password) == 0 or len(name) == 0 or len(dep) == 0:
            QMessageBox.warning(self.Register, '警告', '请补全用户信息！')
            return
        elif not id.isdigit():
            QMessageBox.warning(self.Register, '警告', '学号格式错误！')
            return
        else:
            reader = {'id': id, 'name': name, 'password': password, 'dep': dep, 'user': user}
            try:
                self.Lib_DB.insert_reader(reader)
                QMessageBox.information(self.Register, '通知', '用户注册成功！')
                self.Register.close()
                self.displayReader()

            except Exception as e:
                print(e)

    # 实现借书
    def borrow_book(self):
        ui = self.Reader.readerBorrowReturn
        book_id = ui.borrowIndex.text()
        if len(book_id) == 0:
            QMessageBox.warning(self.Reader, '警告', '请填写借书索引')
        elif not book_id.isdigit():
            QMessageBox.warning(self.Reader, '警告', '索引格式错误')
        else:
            try:
                stu_id = self.CurrentReader
                return_num = self.Lib_DB.book_rent(book_id, stu_id)
                if return_num == 1:
                    QMessageBox.warning(self.Reader, '警告', '未找到要借的图书,请检查索引')
                if return_num == 2:
                    QMessageBox.warning(self.Reader, '警告', '该图书已被借阅')
                if return_num == 3:
                    QMessageBox.information(self.Reader, '通知', '借阅成功！')
                    ui.borrowIndex.clear()
                if return_num == 4:
                    QMessageBox.warning(self.Reader, '警告', '有bug')

                ui.refresh_rent_book_list(stu_id)
            except Exception as e:
                print(e)

    # 实现还书
    def return_book(self):
        ui = self.Reader.readerBorrowReturn
        book_id = ui.returnIndex.text()
        if len(book_id) == 0:
            QMessageBox.warning(self.Reader, '警告', '请填写还书索引')
        elif not book_id.isdigit():
            QMessageBox.warning(self.Reader, '警告', '索引格式错误')
        else:
            try:
                stu_id = self.CurrentReader
                return_num = self.Lib_DB.book_return(book_id, stu_id)
                if return_num == 1:
                    QMessageBox.warning(self.Reader, '警告', '未找到要还的图书,请检查索引')
                if return_num == 2:
                    QMessageBox.warning(self.Reader, '警告', '该图书未被借阅')
                if return_num == 3:
                    QMessageBox.warning(self.Reader, '警告', '无权归还此书')
                if return_num == 4:
                    QMessageBox.information(self.Reader, '通知', '归还成功！')
                    ui.returnIndex.clear()
                if return_num == 5:
                    QMessageBox.warning(self.Reader, '警告', '有bug')

                ui.refresh_rent_book_list(stu_id)
            except Exception as e:
                print(e)


# 管理员登录界面
class LoginAdmin(FramelessWindow, Ui_LoginAdmin):
    def __init__(self, parent=None):
        super(LoginAdmin, self).__init__()

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

        # 设置标题栏
        self.setTitleBar(StandardTitleBar(self))

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.resize((int)(w * 0.8), (int)(h * 0.9))
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


# 读者登录界面
class LoginReader(FramelessWindow, Ui_LoginReader):
    def __init__(self, parent=None):
        super(LoginReader, self).__init__()

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

        # 设置标题栏
        self.setTitleBar(StandardTitleBar(self))

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.resize((int)(w * 0.8), (int)(h * 0.9))
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


# 超级管理员登录界面
class LoginSuper(FramelessWindow, Ui_LoginSuper):
    def __init__(self, parent=None):
        super(LoginSuper, self).__init__()

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

        # 设置标题栏
        self.setTitleBar(StandardTitleBar(self))

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.resize((int)(w * 0.8), (int)(h * 0.9))
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


# 读者注册界面
class Register(QWidget, Ui_Register):
    def __init__(self, parent=None):
        super(Register, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    stats = MainWin()
    stats.show()
    sys.exit(app.exec())
