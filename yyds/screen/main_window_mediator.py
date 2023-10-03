import logging
import re
import threading
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem, QListWidget
from PyQt5.QtWidgets import QMessageBox

from frame.base.wcf_sss import WcfSSS
from frame.constant import Constant
from frame.view.base_qmainwindow_mediator import BaseQMainWindowMediator
from frame.vo.module_vo import ModuleVO
from yyds.aop.permission_aop import permission_wcf, show_message
from yyds.child.aichat_group_window_mediator import AIChatGroupWindowMediator
from yyds.child.job_group_window_mediator import JobGroupWindowMediator
from yyds.child.key_group_window_mediator import KeyGroupWindowMediator
from yyds.child.message_group_window_mediator import MessageGroupWindowMediator
from yyds.child.room_group_window_mediator import RoomGroupWindowMediator
from yyds.child.setting_group_window_mediator import SettingGroupWindowMediator
from yyds.child.switch_group_window_mediator import SwitchGroupWindowMediator
from yyds.screen.main_window import Ui_MainWindow


class MainWindowMediator(BaseQMainWindowMediator):
    NAME = 'MainWindowMediator'
    viewClass = Ui_MainWindow

    def __init__(self, mediatorName=None):
        super(MainWindowMediator, self).__init__(MainWindowMediator.NAME)
        self.selectContracts = {}
        self.LOG = logging.getLogger("MainWindowMediator")
        self.IS_EXIT = False

    def onRegister(self):
        self.LOG.info("MainWindowMediator onRegister")
        self.getViewComponent().version_lable.setText("当前版本:" + Constant.VERSION)

        # 为了释放异步刷新界面的能力
        thread = threading.Thread(target=self.start_handler)
        thread.start()

    def start_handler(self):
        self.getViewComponent().tabListWidget.currentItemChanged.connect(self.item_changed)
        self.getViewComponent().exitButton.clicked.connect(self.log_out)

        self.getViewComponent().refreshPushButton.clicked.connect(self.refresh_contracts_list)
        self.getViewComponent().typComboBox.currentTextChanged.connect(self.change_typeCombobox)
        self.getViewComponent().selAllCheckBox.clicked.connect(self.all_check_contracts)
        # self.getViewComponent().selCheckBox.clicked.connect(self.sel_check_contracts)
        self.getViewComponent().clearPushButton.clicked.connect(self.clear_select_contracts)
        self.getViewComponent().rowListFilterEdit.textChanged.connect(self.on_textChangedL)
        self.getViewComponent().rawListWidget.itemSelectionChanged.connect(self.itemSelectHandler)
        self.getViewComponent().selectListWidget.itemSelectionChanged.connect(self.itemDelHandler)
        self.getViewComponent().SelectListFilterEdit.textChanged.connect(self.on_textChangedR)

        self.getViewComponent().tabListWidget.setCurrentRow(0)

        self.getViewComponent().version_lable.setText("当前版本:" + Constant.VERSION)

    @permission_wcf
    def refresh_contracts_list(self):
        print("refresh_contracts_list click")
        dataList = []
        self.getViewComponent().rawListWidget.clear()

        txt = self.getViewComponent().typComboBox.currentText()
        if txt == "所有联系人":
            dataList = WcfSSS.getInstance().chatRooms + WcfSSS.getInstance().allFriends
        elif txt == "选择群":
            dataList = WcfSSS.getInstance().chatRooms
        elif txt == "选择好友":
            dataList = WcfSSS.getInstance().allFriends

        for data in dataList:
            if data.Remark:
                item = QListWidgetItem(f"[{data.Remark}] {data.NickName}")
            elif data.NickName and not re.match(r'^\s*$', data.NickName):
                item = QListWidgetItem(data.NickName)
            else:
                if data.UserName.endswith("@chatroom") == "选择群":
                    roomName = "[群]" + WcfSSS.getInstance().getChatRoom_Name(data.UserName, 6)
                    if roomName:
                        item = QListWidgetItem(roomName)
                    else:
                        item = QListWidgetItem(data.UserName)
                else:
                    item = QListWidgetItem(data.UserName)
            item.setData(Qt.UserRole, data.UserName)
            self.getViewComponent().rawListWidget.addItem(item)

    def change_typeCombobox(self):
        self.refresh_contracts_list()

    def all_check_contracts(self):
        if self.getViewComponent().selAllCheckBox.isChecked():
            self.getViewComponent().rawListWidget.selectAll()
        else:
            self.getViewComponent().rawListWidget.clearSelection()

    def clear_select_contracts(self):
        """ 清空已选择列表"""
        self.getViewComponent().selectListWidget.clear()
        self.selectContracts = {}
        self.getViewComponent().sel_label.setText("联系人0")

    def add_select_contracts(self):
        """添加选择联系"""
        items = self.getViewComponent().rawListWidget.selectedItems()

        for item in items:
            key = item.data(Qt.UserRole)
            if self.selectContracts.get(key) is None:
                self.selectContracts[key] = item.text()
                self.getViewComponent().selectListWidget.addItem(item.clone())

        if len(items) > 0:
            items = self.getListItems(self.getViewComponent().selectListWidget)
            self.getViewComponent().sel_label.setText(f"联系人{len(items)}")

    def del_select_contracts(self):
        """删除选择的联系人"""
        items = self.getViewComponent().selectListWidget.selectedItems()
        for item in items:
            row = self.getViewComponent().selectListWidget.row(item)
            self.getViewComponent().selectListWidget.takeItem(row)

            key = item.data(Qt.UserRole)
            del self.selectContracts[key]

        self.getViewComponent().sel_label.setText(f"联系人{self.getViewComponent().selectListWidget.count()}")

    def itemSelectHandler(self):
        self.add_select_contracts()

    def itemDelHandler(self):
        self.del_select_contracts()

    def getListItems(self, lw: QListWidget = None):
        if lw is None:
            lw = self.getViewComponent().selectListWidget
        items = []
        for x in range(lw.count()):
            i = lw.item(x)
            if not i.isHidden():
                items.append(i)
        return items

    def on_textChangedL(self, text):
        self.getViewComponent().rawListWidget.clearSelection()
        self._on_text_changed(text, self.getViewComponent().rawListWidget)

    def on_textChangedR(self, text):
        self.getViewComponent().selectListWidget.clearSelection()
        self._on_text_changed(text, self.getViewComponent().selectListWidget)
        items = self.getListItems(self.getViewComponent().selectListWidget)
        self.getViewComponent().sel_label.setText(f"联系{len(items)}")

    def _on_text_changed(self, text, listWidget: QListWidget):
        count = listWidget.count()
        for row in range(count):
            it = listWidget.item(row)
            if text:
                it.setHidden(not self.filter(text, it.text()))
            else:
                it.setHidden(False)

    def filter(self, text, keywords):
        # foo filter
        # in the example the text must be in keywords
        return text in keywords

    def item_changed(self, current, previous):
        print('Current item:', current.text())
        print('Previous item:', previous.text() if previous else 'None')
        if current.text() == "启动":
            module: ModuleVO = ModuleVO(SwitchGroupWindowMediator)
            module.parentUI = self.getViewComponent().stackedWidget
            self.sendNotification(Constant.SWITCH_QWIDGET, module)
        elif current.text() == "消息群发":
            module: ModuleVO = ModuleVO(MessageGroupWindowMediator)
            module.parentUI = self.getViewComponent().stackedWidget
            self.sendNotification(Constant.SWITCH_QWIDGET, module)
        elif current.text() == "定时回复":
            module: ModuleVO = ModuleVO(JobGroupWindowMediator)
            module.parentUI = self.getViewComponent().stackedWidget
            self.sendNotification(Constant.SWITCH_QWIDGET, module)
        elif current.text() == "自动回复":
            module: ModuleVO = ModuleVO(KeyGroupWindowMediator)
            module.parentUI = self.getViewComponent().stackedWidget
            self.sendNotification(Constant.SWITCH_QWIDGET, module)
        elif current.text() == "智能AI聊天":
            module: ModuleVO = ModuleVO(AIChatGroupWindowMediator)
            module.parentUI = self.getViewComponent().stackedWidget
            self.sendNotification(Constant.SWITCH_QWIDGET, module)
        elif current.text() == "群管理":
            module: ModuleVO = ModuleVO(RoomGroupWindowMediator)
            module.parentUI = self.getViewComponent().stackedWidget
            self.sendNotification(Constant.SWITCH_QWIDGET, module)
        elif current.text() == "基础设置":
            module: ModuleVO = ModuleVO(SettingGroupWindowMediator)
            module.parentUI = self.getViewComponent().stackedWidget
            self.sendNotification(Constant.SWITCH_QWIDGET, module)
        elif current.text() == "关于":
            show_message("更多信息，请关注", "https://docs.qq.com/doc/DRVpJdHZUcElsckJU")

    def log_out(self):
        self.close()

    def closeEvent(self, event):
        a = QMessageBox.question(self, '退出', '你确定要退出吗?', QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)  # "退出"代表的是弹出框的标题,"你确认退出.."表示弹出框的内容
        if a == QMessageBox.Yes:
            self.IS_EXIT = True
            wcf = WcfSSS.getInstance()
            if wcf is not None and wcf.is_running():
                self.sendNotification(Constant.STOP_WCF)
                time.sleep(2)
            event.accept()  # 接受关闭事件
            super().closeEvent(event)
        else:
            event.ignore()  # 忽略关闭事件

    def handleNotification(self, notification):
        notName = notification.getName()
        if notName == Constant.UPDATE_USER_VIEW:
            self.refresh_contracts_list()
        elif notName == Constant.STOP_WCF_SUCCESS:
            self.clear_select_contracts()
            self.getViewComponent().rawListWidget.clear()

    def listNotificationInterests(self):
        return [
            Constant.STOP_WCF_SUCCESS,
            Constant.UPDATE_USER_VIEW
        ]

    def onRemove(self):
        self.sendNotification(Constant.CLOSE_CHILD_QWIDGET,
                              [MessageGroupWindowMediator, JobGroupWindowMediator, KeyGroupWindowMediator,
                               AIChatGroupWindowMediator])
        self.LOG.info("MainWindowMediator onRemove")
        pass

    def getViewComponent(self) -> Ui_MainWindow:
        return super().getViewComponent()
