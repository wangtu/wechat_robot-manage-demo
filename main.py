import logging

from frame.appfacade import AppFacade
from frame.constant import Constant
from frame.vo.module_vo import ModuleVO
from yyds.screen.index_window_mediator import IndexWindowMediator

app: AppFacade = AppFacade.getInstance()
app1: AppFacade = AppFacade.getInstance()
LOG = logging.getLogger("main.py")


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


def main():
    app.sendNotification(AppFacade.STARTUP, "hello puremvc")

    module: ModuleVO = ModuleVO(IndexWindowMediator, "pure switchview success")
    # module: ModuleVO = ModuleVO(MainWindowMediator)
    app.sendNotification(Constant.SWITCH_QWIDGET, module)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import Qt

    # 解决界面模糊，缩放比例问题
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # 适应高DPI设备
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # 解决图片在不同分辨率显示模糊问题
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    # 更换windows风格
    # QApplication.setStyle(QStyleFactory.create('windows'))
    qApp = QApplication(sys.argv)
    print_hi('PyCharm')

    main()
    sys.exit(qApp.exec_())
