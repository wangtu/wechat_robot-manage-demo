from PyQt5.QtCore import QThread, pyqtSignal


class SignalThread(QThread):
    signal = pyqtSignal(str)  # 括号里填写信号传递的参数

    def __init__(self):
        super().__init__()
        self.data = None

    def __del__(self):
        # self.wait()
        pass

    def run(self):
        # 进行任务操作
        self.signal.emit(self.data)  # 发射信号
