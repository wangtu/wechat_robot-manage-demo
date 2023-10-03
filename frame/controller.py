import logging

import puremvc.interfaces
import puremvc.patterns.command
from frame.model.config_proxy import ConfigProxy
from frame.model.demo_proxy import DemoProxy
from frame.model.switch_QWidget_proxy import SwitchQWidgetProxy
from frame.view.wcf_mediator import WcfMediator

LOG = logging.getLogger("controller.py")


class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, notification):
        LOG.info("StartupCommand start!")
        # 初始化config.yaml，并实例化日志
        self.facade.registerProxy(ConfigProxy())
        self.facade.registerProxy(DemoProxy())
        # 核心类，实现pyqt的UI初始化、关联mediator
        self.facade.registerProxy(SwitchQWidgetProxy())
        # 微信端控制mediator
        self.facade.registerMediator(WcfMediator())
        LOG.info("StartupCommand complete!")


class SwitchQWidgetCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, notification):
        switchModuleProxy: SwitchQWidgetProxy = self.facade.retrieveProxy(SwitchQWidgetProxy.NAME)
        switchModuleProxy.loadQWidgetWindow(notification.getBody())


class CloseQWidgetCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, notification):
        switchModuleProxy: SwitchQWidgetProxy = self.facade.retrieveProxy(SwitchQWidgetProxy.NAME)
        switchModuleProxy.closeQWidgetWindow(notification.getBody())


class CloseChildQWidgetCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, notification):
        switchModuleProxy: SwitchQWidgetProxy = self.facade.retrieveProxy(SwitchQWidgetProxy.NAME)
        switchModuleProxy.closeChildQWidget(notification.getBody())
