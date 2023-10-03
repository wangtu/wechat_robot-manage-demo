from PyQt5.QtWidgets import QWidget

from frame.constant import Constant
from puremvc.interfaces import IMediator
from puremvc.patterns.mediator import Mediator


class BaseQWidgetMediator(Mediator, IMediator, QWidget):
    NAME = 'ScreenBaseMediator'
    data: any = None  # 数据
    viewClass: QWidget = None  # UI界面

    def __init__(self, mediatorName=None):
        Mediator.__init__(self, mediatorName, None)
        QWidget.__init__(self)

    def onRegister(self):
        print("ScreenBaseMediator onRegister")

    def getSelectListWidget(self):
        """业务放这里虽然不合理，但是此项目是很方便"""
        from yyds.screen.main_window_mediator import MainWindowMediator
        mediator: MainWindowMediator = self.facade.retrieveMediator(MainWindowMediator.NAME)
        return mediator.getListItems()

    def closeEvent(self, event):
        """继承QWidget，实现关闭自身UI，以及对应的mediator"""
        print("BaseQWidgetMediator closeEvent received!")
        self.sendNotification(Constant.CLOSE_QWIDGET, self)

    def onRemove(self):
        print("ScreenBaseMediator onRemove")
