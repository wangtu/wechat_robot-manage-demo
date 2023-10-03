from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from frame.base.signal_thread_tuple import SignalThreadTuple
from frame.base.wcf_sss import WcfSSS


def permission_wcf(func):
    """切面权限判断，必须先启动wcf才允许操作函数"""

    def wrapper(self, *args, **kwargs):
        if WcfSSS.getInstance() is None:
            show_message("提示", "请先到tab启动页首次启动程序")
            return
        if not WcfSSS.getInstance().is_running():
            show_message("提示", "请先到tab启动页重新启动程序")
            return

        res = func(self)
        return res

    return wrapper


def show_message(title, content):
    # 异步刷新界面，为了性能，可读性是弱了点
    done_thread.data = (title, content)
    done_thread.start()


def show_message2(data):
    msg_box = QMessageBox(QMessageBox.Question, data[0], data[1])  # 退出表示弹出框标题，"你确定退出吗？"表示弹出框的内容
    msg_box.setTextInteractionFlags(Qt.TextSelectableByMouse)
    msg_box.exec_()  # 执行弹出框


done_thread = SignalThreadTuple()
done_thread.signal.connect(show_message2)
