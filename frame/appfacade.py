from frame import controller
from frame.constant import Constant
from puremvc.patterns.facade import Facade


class AppFacade(Facade):
    STARTUP: str = "startup"

    def __init__(self) -> None:
        self.initializeFacade()

    @staticmethod
    def getInstance():
        return AppFacade()

    def initializeFacade(self) -> None:
        super(AppFacade, self).initializeFacade()
        self.initializeController()

    def initializeController(self) -> None:
        super(AppFacade, self).initializeController()

        super(AppFacade, self).registerCommand(AppFacade.STARTUP, controller.StartupCommand)
        super(AppFacade, self).registerCommand(Constant.SWITCH_QWIDGET, controller.SwitchQWidgetCommand)
        super(AppFacade, self).registerCommand(Constant.CLOSE_QWIDGET, controller.CloseQWidgetCommand)
        super(AppFacade, self).registerCommand(Constant.CLOSE_CHILD_QWIDGET, controller.CloseChildQWidgetCommand)


if __name__ == '__main__':
    print(f'Hi, app-facade')
