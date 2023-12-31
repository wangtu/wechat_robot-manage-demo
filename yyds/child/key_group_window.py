# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key_group_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(437, 528)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.key_count_label = QtWidgets.QLabel(Form)
        self.key_count_label.setObjectName("key_count_label")
        self.verticalLayout.addWidget(self.key_count_label)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(100, 0))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pdelButton = QtWidgets.QPushButton(Form)
        self.pdelButton.setObjectName("pdelButton")
        self.verticalLayout.addWidget(self.pdelButton)
        self.line = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(20, 2))
        self.line.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioEqButton = QtWidgets.QRadioButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioEqButton.sizePolicy().hasHeightForWidth())
        self.radioEqButton.setSizePolicy(sizePolicy)
        self.radioEqButton.setMinimumSize(QtCore.QSize(0, 0))
        self.radioEqButton.setChecked(False)
        self.radioEqButton.setObjectName("radioEqButton")
        self.horizontalLayout_2.addWidget(self.radioEqButton)
        self.radioHasButton = QtWidgets.QRadioButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioHasButton.sizePolicy().hasHeightForWidth())
        self.radioHasButton.setSizePolicy(sizePolicy)
        self.radioHasButton.setMinimumSize(QtCore.QSize(0, 0))
        self.radioHasButton.setObjectName("radioHasButton")
        self.horizontalLayout_2.addWidget(self.radioHasButton)
        self.radioReButton = QtWidgets.QRadioButton(Form)
        self.radioReButton.setMinimumSize(QtCore.QSize(0, 0))
        self.radioReButton.setObjectName("radioReButton")
        self.horizontalLayout_2.addWidget(self.radioReButton)
        self.atCheckBox = QtWidgets.QCheckBox(Form)
        self.atCheckBox.setObjectName("atCheckBox")
        self.horizontalLayout_2.addWidget(self.atCheckBox)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.keyLineEdit = QtWidgets.QLineEdit(Form)
        self.keyLineEdit.setInputMask("")
        self.keyLineEdit.setText("")
        self.keyLineEdit.setMaxLength(500)
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.horizontalLayout.addWidget(self.keyLineEdit)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.noRadioButton = QtWidgets.QRadioButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noRadioButton.sizePolicy().hasHeightForWidth())
        self.noRadioButton.setSizePolicy(sizePolicy)
        self.noRadioButton.setMinimumSize(QtCore.QSize(50, 0))
        self.noRadioButton.setChecked(True)
        self.noRadioButton.setObjectName("noRadioButton")
        self.horizontalLayout_12.addWidget(self.noRadioButton)
        self.atOneRadioButton = QtWidgets.QRadioButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atOneRadioButton.sizePolicy().hasHeightForWidth())
        self.atOneRadioButton.setSizePolicy(sizePolicy)
        self.atOneRadioButton.setMinimumSize(QtCore.QSize(50, 0))
        self.atOneRadioButton.setObjectName("atOneRadioButton")
        self.horizontalLayout_12.addWidget(self.atOneRadioButton)
        self.atAllRadioButton = QtWidgets.QRadioButton(Form)
        self.atAllRadioButton.setMinimumSize(QtCore.QSize(50, 0))
        self.atAllRadioButton.setObjectName("atAllRadioButton")
        self.horizontalLayout_12.addWidget(self.atAllRadioButton)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 150))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txtPlainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.txtPlainTextEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.txtPlainTextEdit.setAutoFillBackground(False)
        self.txtPlainTextEdit.setMaximumBlockCount(15)
        self.txtPlainTextEdit.setObjectName("txtPlainTextEdit")
        self.horizontalLayout_4.addWidget(self.txtPlainTextEdit)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.imgPlainTextEdit = QtWidgets.QPlainTextEdit(self.tab_4)
        self.imgPlainTextEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.imgPlainTextEdit.setMaximumBlockCount(15)
        self.imgPlainTextEdit.setObjectName("imgPlainTextEdit")
        self.horizontalLayout_6.addWidget(self.imgPlainTextEdit)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.filePlainTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.filePlainTextEdit.setMaximumBlockCount(15)
        self.filePlainTextEdit.setObjectName("filePlainTextEdit")
        self.horizontalLayout_7.addWidget(self.filePlainTextEdit)
        self.tabWidget.addTab(self.tab_3, "")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        self.rangeComboBox = QtWidgets.QComboBox(Form)
        self.rangeComboBox.setObjectName("rangeComboBox")
        self.rangeComboBox.addItem("")
        self.rangeComboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rangeComboBox)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.addBtn = QtWidgets.QPushButton(Form)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout.addWidget(self.addBtn)
        self.horizontalLayout_21.addLayout(self.verticalLayout)
        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22.setStretch(0, 2)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.key_count_label.setText(_translate("Form", "关键词侦听"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "群/好友"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "关键字"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "关键词类型"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "提问需要@"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "回复内容"))
        self.pdelButton.setText(_translate("Form", "选中删除"))
        self.label_7.setText(_translate("Form", "侦听类型"))
        self.radioEqButton.setText(_translate("Form", "等于"))
        self.radioHasButton.setText(_translate("Form", "包含"))
        self.radioReButton.setText(_translate("Form", "正则表达式"))
        self.atCheckBox.setText(_translate("Form", "群被人@"))
        self.label_6.setText(_translate("Form", "侦听内容"))
        self.keyLineEdit.setPlaceholderText(_translate("Form", "输入关键字，如：你是谁"))
        self.label.setText(_translate("Form", "群回复时"))
        self.noRadioButton.setText(_translate("Form", "直接回复"))
        self.atOneRadioButton.setText(_translate("Form", "@提问者"))
        self.atAllRadioButton.setText(_translate("Form", "@所有(群主)"))
        self.txtPlainTextEdit.setPlaceholderText(_translate("Form", "回复文本内容"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "文本"))
        self.imgPlainTextEdit.setPlaceholderText(
            _translate("Form", "回复图片路径，如C:\\Users\\wangtu\\Pictures\\Default.jpg"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "图片"))
        self.filePlainTextEdit.setPlaceholderText(
            _translate("Form", "回复文件路径，如C:\\Users\\wangtu\\Pictures\\file.txt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "文件"))
        self.rangeComboBox.setItemText(0, _translate("Form", "左侧列表的群和好友"))
        self.rangeComboBox.setItemText(1, _translate("Form", "全部群和好友"))
        self.label_2.setText(_translate("Form", "侦听对象"))
        self.addBtn.setText(_translate("Form", "添加关键词监控"))
