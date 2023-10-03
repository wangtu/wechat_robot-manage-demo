import logging

from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from yyds.child.aichat_group_window import Ui_Form


class AIChatGroupWindowMediator(BaseQWidgetMediator):
    NAME = 'AIChatGroupWindowMediator'
    viewClass = Ui_Form

    def __init__(self, mediatorName=None):
        super(AIChatGroupWindowMediator, self).__init__(AIChatGroupWindowMediator.NAME)
        self.LOG = logging.getLogger("AIChatGroupWindowMediator")

    def onRegister(self):
        self.LOG.info("AIChatGroupWindowMediator onRegister")

    def onRemove(self):
        self.LOG.info("AIChatGroupWindowMediator onRemove")
        pass

    def getViewComponent(self) -> Ui_Form:
        return super().getViewComponent()
