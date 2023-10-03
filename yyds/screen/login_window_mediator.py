import logging

from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from yyds.screen.login_window import Ui_Form


class LoginWindowMediator(BaseQWidgetMediator):
    NAME = 'LoginWindowMediator'
    viewClass = Ui_Form

    def __init__(self, mediatorName=None):
        super(LoginWindowMediator, self).__init__(LoginWindowMediator.NAME)
        self.LOG = logging.getLogger("LoginWindowMediatorMediator")

    def onRegister(self):
        pass

    def onRemove(self):
        self.LOG.info("LoginWindowMediatorMediator onRemove")
        pass
