# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message_group_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(374, 432)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.message_count_label = QtWidgets.QLabel(Form)
        self.message_count_label.setStyleSheet("")
        self.message_count_label.setObjectName("message_count_label")
        self.verticalLayout.addWidget(self.message_count_label)
        self.logPlainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.logPlainTextEdit.setReadOnly(True)
        self.logPlainTextEdit.setPlainText("")
        self.logPlainTextEdit.setMaximumBlockCount(6000)
        self.logPlainTextEdit.setObjectName("logPlainTextEdit")
        self.verticalLayout.addWidget(self.logPlainTextEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.imgPushButton = QtWidgets.QPushButton(Form)
        self.imgPushButton.setObjectName("imgPushButton")
        self.horizontalLayout_4.addWidget(self.imgPushButton)
        self.filePushButton = QtWidgets.QPushButton(Form)
        self.filePushButton.setEnabled(True)
        self.filePushButton.setObjectName("filePushButton")
        self.horizontalLayout_4.addWidget(self.filePushButton)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wxTextEdit = QtWidgets.QTextEdit(Form)
        self.wxTextEdit.setEnabled(True)
        self.wxTextEdit.setObjectName("wxTextEdit")
        self.horizontalLayout.addWidget(self.wxTextEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.wxTextPushButton = QtWidgets.QPushButton(Form)
        self.wxTextPushButton.setObjectName("wxTextPushButton")
        self.verticalLayout_2.addWidget(self.wxTextPushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.message_count_label.setText(_translate("Form", "新消息"))
        self.imgPushButton.setText(_translate("Form", "发送图片"))
        self.filePushButton.setText(_translate("Form", "发送文件"))
        self.pushButton_5.setText(_translate("Form", "功能待定"))
        self.wxTextEdit.setPlaceholderText(
            _translate("Form", "选择列表后，输入要群发的文字或选择图片、文件。Shift+Enter换行，Enter发送"))
        self.wxTextPushButton.setText(_translate("Form", "发送/Enter"))
