import logging

from PyQt5.QtWidgets import QWidget, QStackedWidget

import puremvc.patterns.proxy
from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from frame.vo.module_vo import ModuleVO


class SwitchQWidgetProxy(puremvc.patterns.proxy.Proxy):
    NAME = "SwitchModuleProxy"

    def __init__(self, proxyName=None, data=None):
        super(SwitchQWidgetProxy, self).__init__(SwitchQWidgetProxy.NAME, [])
        self.LOG = logging.getLogger("SwitchQWidgetProxy")

        self.moduleDic = {}

    def onRegister(self):
        print("SwitchQWidgetProxy onRegister")

    def loadQWidgetWindow(self, module: ModuleVO):
        baseQWidgetMediator: BaseQWidgetMediator = self.moduleDic.get(str(module.mediatorClass))
        if baseQWidgetMediator is not None:
            print(f"{str(module.mediatorClass)} 已实例化，请勿重复请求")
            if isinstance(module.parentUI, QStackedWidget):
                module.parentUI.setCurrentWidget(baseQWidgetMediator)
            baseQWidgetMediator.show()
            return

        if module.mediatorClass.NAME is not None:
            baseQWidgetMediator = module.mediatorClass()
            # 实例化界面
            mainWindow: QWidget = baseQWidgetMediator.viewClass()
            self.moduleDic[str(module.mediatorClass)] = baseQWidgetMediator
            mainWindow.setupUi(baseQWidgetMediator)
            baseQWidgetMediator.show()

            if module.parentUI is not None:
                if isinstance(module.parentUI, QStackedWidget):
                    module.parentUI.addWidget(baseQWidgetMediator)
                    module.parentUI.setCurrentWidget(baseQWidgetMediator)
                elif isinstance(module.parentUI, QWidget):
                    module.parentUI.addWidget(baseQWidgetMediator)

            baseQWidgetMediator.setViewComponent(mainWindow)
            baseQWidgetMediator.data = module.data
            self.__registerMediator(baseQWidgetMediator, module)

    def closeQWidgetWindow(self, baseQWidgetMediator: BaseQWidgetMediator):
        self.LOG.info("closeQWidgetWindow！")
        self.facade.removeMediator(baseQWidgetMediator.getMediatorName())
        viewClass = str(type(baseQWidgetMediator))
        self.LOG.info(type(baseQWidgetMediator))
        if self.moduleDic.get(viewClass) is not None:
            print("删除字典")
            del self.moduleDic[viewClass]

        baseQWidgetMediator.close()

    def closeChildQWidget(self, _list: list):
        for baseQWidgetMediatorClass in _list:
            self.LOG.info("closeChildQWidget！" + baseQWidgetMediatorClass.NAME)
            self.facade.removeMediator(baseQWidgetMediatorClass.NAME)
            if self.moduleDic.get(str(baseQWidgetMediatorClass)) is not None:
                print("删除字典")
                del self.moduleDic[str(baseQWidgetMediatorClass)]

    def __registerMediator(self, baseMediator: BaseQWidgetMediator, vo: ModuleVO) -> bool:
        if self.facade.hasMediator(baseMediator.getMediatorName()):
            self.LOG.info("已经注册")
            pass
        else:
            self.facade.registerMediator(baseMediator)

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
