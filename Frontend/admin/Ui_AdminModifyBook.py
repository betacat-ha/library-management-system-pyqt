# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminModifyBook.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminModifyBook(object):
    def setupUi(self, AdminModifyBook):
        AdminModifyBook.setObjectName("AdminModifyBook")
        AdminModifyBook.resize(590, 426)
        self.horizontalLayout = QtWidgets.QHBoxLayout(AdminModifyBook)
        self.horizontalLayout.setContentsMargins(-1, 35, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitleLabel = TitleLabel(AdminModifyBook)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout_2.addWidget(self.TitleLabel)
        self.CardWidget = CardWidget(AdminModifyBook)
        self.CardWidget.setObjectName("CardWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CardWidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.CardWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.CardWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.CardWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.CardWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.bookTitle = LineEdit(self.CardWidget)
        self.bookTitle.setObjectName("bookTitle")
        self.verticalLayout_8.addWidget(self.bookTitle)
        self.bookIndex = LineEdit(self.CardWidget)
        self.bookIndex.setObjectName("bookIndex")
        self.verticalLayout_8.addWidget(self.bookIndex)
        self.bookAuthor = LineEdit(self.CardWidget)
        self.bookAuthor.setObjectName("bookAuthor")
        self.verticalLayout_8.addWidget(self.bookAuthor)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.publishYear = LineEdit(self.CardWidget)
        self.publishYear.setObjectName("publishYear")
        self.horizontalLayout_5.addWidget(self.publishYear)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.modifyButton = PrimaryPushButton(self.CardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modifyButton.sizePolicy().hasHeightForWidth())
        self.modifyButton.setSizePolicy(sizePolicy)
        self.modifyButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.modifyButton.setObjectName("modifyButton")
        self.horizontalLayout_7.addWidget(self.modifyButton)
        self.resetButton = PushButton(self.CardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        self.resetButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_7.addWidget(self.resetButton)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.CardWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(AdminModifyBook)
        QtCore.QMetaObject.connectSlotsByName(AdminModifyBook)

    def retranslateUi(self, AdminModifyBook):
        _translate = QtCore.QCoreApplication.translate
        AdminModifyBook.setWindowTitle(_translate("AdminModifyBook", "书刊查找"))
        self.TitleLabel.setText(_translate("AdminModifyBook", "修改图书信息"))
        self.label_11.setText(_translate("AdminModifyBook", "书   名："))
        self.label_12.setText(_translate("AdminModifyBook", "索引号："))
        self.label_13.setText(_translate("AdminModifyBook", "作   者："))
        self.label_14.setText(_translate("AdminModifyBook", "出版时间："))
        self.modifyButton.setText(_translate("AdminModifyBook", "修改"))
        self.resetButton.setText(_translate("AdminModifyBook", "重置"))
from qfluentwidgets import CardWidget, LineEdit, PrimaryPushButton, PushButton, TitleLabel
