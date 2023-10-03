import logging

from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from yyds.child.job_group_window import Ui_Form


class JobGroupWindowMediator(BaseQWidgetMediator):
    NAME = 'JobGroupWindowMediator'
    viewClass = Ui_Form

    def __init__(self, mediatorName=None):
        super(JobGroupWindowMediator, self).__init__(JobGroupWindowMediator.NAME)
        self.LOG = logging.getLogger("JobGroupWindowMediator")

    def onRegister(self):
        self.LOG.info("JobGroupWindowMediator onRegister")

    def onRemove(self):
        self.LOG.info("JobGroupWindowMediator onRemove")
        pass

    def getViewComponent(self) -> Ui_Form:
        return super().getViewComponent()
