from PyQt5.QtWidgets import QMainWindow

from frame.constant import Constant
from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from puremvc.patterns.mediator import Mediator


class BaseQMainWindowMediator(QMainWindow, BaseQWidgetMediator):
    NAME = 'BaseQMainWindowMediator'

    def __init__(self, mediatorName=None):
        QMainWindow.__init__(self)
        Mediator.__init__(self, mediatorName, None)

    def onRegister(self):
        self.LOG.info("MainWindowMediator onRegister")
        pass

    def closeEvent(self, event):
        """继承QWidget，实现关闭自身UI，以及对应的mediator"""
        print("BaseQMainWindowMediator closeEvent received!")
        self.sendNotification(Constant.CLOSE_QWIDGET, self)

    def onRemove(self):
        pass
