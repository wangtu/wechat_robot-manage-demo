import logging

from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from yyds.child.room_group_window import Ui_Form


class RoomGroupWindowMediator(BaseQWidgetMediator):
    NAME = 'RoomGroupWindowMediator'
    viewClass = Ui_Form

    def __init__(self, mediatorName=None):
        super(RoomGroupWindowMediator, self).__init__(RoomGroupWindowMediator.NAME)
        self.LOG = logging.getLogger("RoomGroupWindowMediator")

    def onRegister(self):
        self.LOG.info("RoomGroupWindowMediator onRegister")

    def onRemove(self):
        self.LOG.info("RoomGroupWindowMediator onRemove")
        pass

    def getViewComponent(self) -> Ui_Form:
        return super().getViewComponent()
