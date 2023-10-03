from PyQt5.QtWidgets import QWidget

from frame.view.base_qwidget_mediator import BaseQWidgetMediator


class ModuleVO:

    def __init__(self, mediatorClass: BaseQWidgetMediator, data: any = None):
        # 传递class类，通常是继承 baseQWidgetMediator
        # from frame.view.screen_base_mediator import BaseQWidgetMediator
        self.mediatorClass = mediatorClass
        # 已实例化的父容器，非必传
        self.parentUI: QWidget = None
        # 携带的参数
        self.data = data

    # # 携带的参数
    # data: any = None
    # # 传递class类
    # mediatorClass: ScreenBaseMediator = None
