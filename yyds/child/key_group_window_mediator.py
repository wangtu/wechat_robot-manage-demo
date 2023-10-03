import logging

from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from yyds.child.key_group_window import Ui_Form


class KeyGroupWindowMediator(BaseQWidgetMediator):
    NAME = 'KeyGroupWindowMediator'
    viewClass = Ui_Form

    def __init__(self, mediatorName=None):
        super(KeyGroupWindowMediator, self).__init__(KeyGroupWindowMediator.NAME)
        self.LOG = logging.getLogger("KeyGroupWindowMediator")

    def onRegister(self):
        self.LOG.info("KeyGroupWindowMediator onRegister")

    def onRemove(self):
        self.LOG.info("KeyGroupWindowMediator onRemove")
        pass

    def getViewComponent(self) -> Ui_Form:
        return super().getViewComponent()
