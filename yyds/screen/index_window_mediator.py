import logging
import os
import signal
import time
import webbrowser

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication

from frame.constant import Constant
from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from frame.vo.module_vo import ModuleVO
from util.software_manager import SoftwareManager
from yyds.aop.permission_aop import show_message
from yyds.screen.index_window import Ui_Form
from yyds.screen.main_window_mediator import MainWindowMediator


class IndexWindowMediator(BaseQWidgetMediator):
    NAME = 'IndexWindowMediator'
    viewClass = Ui_Form

    def __init__(self, mediatorName=None):
        super(IndexWindowMediator, self).__init__(IndexWindowMediator.NAME)
        self.LOG = logging.getLogger("IndexWindowMediator")

    def onRegister(self):
        self.getViewComponent().checkButton.clicked.connect(self.testEnvironment)
        self.getViewComponent().cleanPortButton.clicked.connect(self.cleanPortHandler)
        self.getViewComponent().downButton.clicked.connect(self.openDownUrl)
        self.getViewComponent().login_pushButton.clicked.connect(self.loginMain)
        self.getViewComponent().note_label.mouseReleaseEvent = self.open_webpage

    def open_webpage(self, event):
        url = "https://docs.qq.com/doc/DRVhaVU9Qa0tFU050"
        webbrowser.open(url)

    def testEnvironment(self):
        self.LOG.info("检查环境变量")
        step1: str = "-> 1- 检查环境依赖端口 " + str(Constant.WCF_PORT) + " 占用情况"
        self.getViewComponent().textEdit.append(step1)
        QApplication.processEvents()
        time.sleep(0.5)
        self.getViewComponent().textEdit.append(self.checkPortToStr(Constant.WCF_PORT))

        step1 = "\n-> 2- 检查环境依赖端口 " + str(Constant.WCF_PORT + 1) + " 占用情况"
        self.getViewComponent().textEdit.append(step1)
        QApplication.processEvents()

        time.sleep(0.5)
        self.getViewComponent().textEdit.append(self.checkPortToStr(Constant.WCF_PORT + 1))

        step1 = "\n-> 3- 检查微信版本号 "
        self.getViewComponent().textEdit.append(step1)
        QApplication.processEvents()

        time.sleep(0.5)
        manager = SoftwareManager()
        # 通过名字获取
        wechat = manager.get_by_name("微信")
        step1 = "-> " + wechat['DisplayName'] + "  " + wechat['DisplayVersion'] + "  " + wechat['InstallLocation']
        self.getViewComponent().textEdit.append(step1)

        if Constant.WECHAT_VERSION == wechat['DisplayVersion']:
            step1 = "-> 微信版本符合环境要求  √"
        else:
            step1 = "-> !!!注意！，微信版本不符合环境要求，需要安装:" + Constant.WECHAT_VERSION + "  ×"
        self.getViewComponent().textEdit.append(step1)

    @staticmethod
    def checkPortToStr(port: int) -> str:
        res_list = IndexWindowMediator.checkPort(port)
        if len(res_list) > 0:
            res = "-> !!!注意，依赖端口" + str(Constant.WCF_PORT) + "已被占用 ×"
        else:
            res = "-> 环境端口 " + str(Constant.WCF_PORT) + " 空闲，检测OK √"
        return res

    @staticmethod
    def checkPort(port: int) -> str:
        res_list = []
        # 判断端口是否被占用，占用直接把占用端口的进程给杀掉
        with os.popen(f'netstat -aon|findstr "{port}"') as res:
            res = res.read().split('\n')
            for line in res:
                temp = [i for i in line.split(' ') if i != '']
                if len(temp) > 4 and int(temp[4]) > 1:
                    res_list.append(temp[4])

        return res_list

    def cleanPortHandler(self):
        self.cleanPort(Constant.WCF_PORT)
        self.cleanPort(Constant.WCF_PORT + 1)

    def cleanPort(self, port: int = Constant.WCF_PORT):
        # 判断端口是否被占用，占用直接把占用端口的进程给杀掉
        res_list = IndexWindowMediator.checkPort(port)
        if len(res_list) > 0:
            for i in res_list:
                os.kill(int(i), signal.SIGINT)
                print(f"杀死占用端口的进程成功，该进程pid：{i}")
                tip = "被占用端口" + str(port) + "的进程成功清理，该进程pid：" + str(i)

        else:
            tip = str(port) + "端口没有被占用，无需清理"
        self.getViewComponent().textEdit.append(tip)

    @staticmethod
    def openDownUrl():
        QDesktopServices.openUrl(QUrl("https://www.gpsmap.cc/soft/121596.html"))

    def loginMain(self):
        ischeck = self.getViewComponent().yes_checkBox.isChecked()
        if not ischeck:
            show_message("提示", "请阅读服务和隐私协议，并确定勾选同意")
            return

        module: ModuleVO = ModuleVO(MainWindowMediator)
        self.sendNotification(Constant.SWITCH_QWIDGET, module)
        self.close()

    def onRemove(self):
        self.LOG.info("IndexWindowMediator onRemove")
        pass

    def getViewComponent(self) -> Ui_Form:
        return super().getViewComponent()
