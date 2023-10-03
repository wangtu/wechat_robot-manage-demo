import logging
import os
import signal

from frame.base.log_handler import MyLogHandler
from frame.base.signal_thread import SignalThread
from frame.base.wcf_sss import WcfSSS
from frame.constant import Constant
from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from yyds.child.switch_group_window import Ui_Form

"""
tab - 启动的主控制器
"""


class SwitchGroupWindowMediator(BaseQWidgetMediator):
    NAME = 'SwitchGroupWindowMediator'
    viewClass = Ui_Form

    def __init__(self, mediatorName=None):
        super(SwitchGroupWindowMediator, self).__init__(SwitchGroupWindowMediator.NAME)
        self.LOG = logging.getLogger("SwitchGroupWindowMediator")
        self.maximum_block_count: int = 1000

        self.log_done_thread = SignalThread()
        self.log_done_thread.signal.connect(self.receiveSignal)

    def onRegister(self):
        self.LOG.info("SwitchGroupWindowMediator onRegister")
        self.getViewComponent().startButton.clicked.connect(self.startHandler)
        self.getViewComponent().stopButton.clicked.connect(self.stopHandler)
        self.getViewComponent().clear_pushButton.clicked.connect(self.clearHandler)
        self.getViewComponent().debugTextEdit.setMaximumBlockCount(self.maximum_block_count)
        myLogHandler = MyLogHandler.getInstance()
        myLogHandler.callbackFunc = self.refreshConsole

    def refreshConsole(self, record):
        """控制台日志文本刷新"""
        self.log_done_thread.data = record
        self.log_done_thread.start()

    def receiveSignal(self, text):
        """异步线程实现刷新UI界面"""
        # 槽函数
        self.getViewComponent().debugTextEdit.appendPlainText(text)

    # @thread_check(True)
    def startHandler(self):
        try:
            self.cleanPortHandler()
            self.sendNotification(Constant.START_WCF)
            self.getViewComponent().startButton.setEnabled(False)
            self.getViewComponent().stopButton.setEnabled(True)
        except Exception as e:
            print(e)

    def stopHandler(self):
        self.sendNotification(Constant.STOP_WCF)
        self.getViewComponent().startButton.setEnabled(True)
        self.getViewComponent().stopButton.setEnabled(False)

    def cleanPortHandler(self):
        self.cleanPort(Constant.WCF_PORT)
        self.cleanPort(Constant.WCF_PORT + 1)

    def checkPort(self, port: int) -> list:
        res_list = []
        # 判断端口是否被占用，占用直接把占用端口的进程给杀掉
        with os.popen(f'netstat -aon|findstr "{port}"') as res:
            res = res.read().split('\n')
            for line in res:
                temp = [i for i in line.split(' ') if i != '']
                if len(temp) > 4 and int(temp[4]) > 1:
                    res_list.append(temp[4])
        return res_list

    def cleanPort(self, port: int = Constant.WCF_PORT):
        # 判断端口是否被占用，占用直接把占用端口的进程给杀掉
        res_list = self.checkPort(port)
        try:
            if len(res_list) > 0:
                for i in res_list:
                    print(f"os kill {i}")
                    os.kill(int(i), signal.SIGINT)
        except Exception as e:
            print(e)

    def clearHandler(self):
        self.getViewComponent().debugTextEdit.clear()

    def handleNotification(self, notification):
        notName = notification.getName()
        if notName == Constant.START_WCF_SUCCESS:
            wcf: WcfSSS = notification.getBody()
            try:
                self.getViewComponent().wxIdEdit.setText(wcf.userInfo.get("wxid"))
                self.getViewComponent().wxNameEdit.setText(wcf.userInfo.get("name"))
                self.getViewComponent().mobileEdit.setText(wcf.userInfo.get("mobile"))
                self.getViewComponent().roomLenEdit.setText(str(len(wcf.chatRooms)))
                self.getViewComponent().friendLenEdit.setText(str(len(wcf.allFriends)))
            except Exception as e:
                self.LOG.info("捕获错误", str(e))
            wxid = wcf.userInfo.get("wxid")
            self.LOG.info(f"正在读取 {wxid} 角色权限")
            name = wcf.userInfo.get("name")
            mobile = wcf.userInfo.get("mobile")
            # 刷新main主界面
            self.sendNotification(Constant.UPDATE_USER_VIEW)
            self.LOG.info(f"{wxid} 角色权限获取成功")

        elif notName == Constant.STOP_WCF_SUCCESS:
            self.getViewComponent().wxIdEdit.setText("")
            self.getViewComponent().wxNameEdit.setText("")
            self.getViewComponent().mobileEdit.setText("")
            self.getViewComponent().roomLenEdit.setText("")
            self.getViewComponent().friendLenEdit.setText("")

    def listNotificationInterests(self):
        return [
            Constant.START_WCF_SUCCESS,
            Constant.STOP_WCF_SUCCESS
        ]

    def onRemove(self):
        self.LOG.info("SwitchGroupWindowMediator onRemove")
        pass

    def getViewComponent(self) -> Ui_Form:
        return super().getViewComponent()
