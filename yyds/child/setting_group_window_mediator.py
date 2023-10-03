import logging

from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from yyds.child.setting_group_window import Ui_Form


class SettingGroupWindowMediator(BaseQWidgetMediator):
    NAME = 'SettingGroupWindowMediator'
    viewClass = Ui_Form

    def __init__(self, mediatorName=None):
        super(SettingGroupWindowMediator, self).__init__(SettingGroupWindowMediator.NAME)
        self.LOG = logging.getLogger("SettingGroupWindowMediator")

    def onRegister(self):
        self.LOG.info("SettingGroupWindowMediator onRegister")

    def onRemove(self):
        self.LOG.info("SettingGroupWindowMediator onRemove")
        pass

    def getViewComponent(self) -> Ui_Form:
        return super().getViewComponent()
