# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\everything.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 291)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_find = QtWidgets.QPushButton(Dialog)
        self.pushButton_find.setMinimumSize(QtCore.QSize(0, 5))
        self.pushButton_find.setObjectName("pushButton_find")
        self.gridLayout.addWidget(self.pushButton_find, 1, 1, 1, 1)
        self.pushButton_select = QtWidgets.QPushButton(Dialog)
        self.pushButton_select.setMinimumSize(QtCore.QSize(0, 5))
        self.pushButton_select.setObjectName("pushButton_select")
        self.gridLayout.addWidget(self.pushButton_select, 0, 1, 1, 1)
        self.textEdit_filePattern = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_filePattern.sizePolicy().hasHeightForWidth())
        self.textEdit_filePattern.setSizePolicy(sizePolicy)
        self.textEdit_filePattern.setMinimumSize(QtCore.QSize(200, 35))
        self.textEdit_filePattern.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_filePattern.setObjectName("textEdit_filePattern")
        self.gridLayout.addWidget(self.textEdit_filePattern, 1, 0, 1, 1)
        self.textEdit_dir = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_dir.sizePolicy().hasHeightForWidth())
        self.textEdit_dir.setSizePolicy(sizePolicy)
        self.textEdit_dir.setMinimumSize(QtCore.QSize(0, 35))
        self.textEdit_dir.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_dir.setObjectName("textEdit_dir")
        self.gridLayout.addWidget(self.textEdit_dir, 0, 0, 1, 1)
        self.listWidget_result = QtWidgets.QListWidget(Dialog)
        self.listWidget_result.setObjectName("listWidget_result")
        self.gridLayout.addWidget(self.listWidget_result, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_find.setText(_translate("Dialog", "🔍"))
        self.pushButton_select.setText(_translate("Dialog", "浏览"))
        self.textEdit_filePattern.setPlaceholderText(_translate("Dialog", "文件Pattern"))
        self.textEdit_dir.setPlaceholderText(_translate("Dialog", "查找路径"))
