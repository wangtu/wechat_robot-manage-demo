import logging
import random
import threading
import time

from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from frame.base.signal_thread import SignalThread
from frame.base.wcf_sss import WcfSSS
from frame.constant import Constant
from frame.view.base_qwidget_mediator import BaseQWidgetMediator
from frame.vo.wx_text_vo import WxTextVO
from yyds.aop.permission_aop import permission_wcf, show_message
from yyds.child.message_group_window import Ui_Form

"""
tab 消息群发控制器
"""


class MessageGroupWindowMediator(BaseQWidgetMediator):
    NAME = 'MessageGroupWindowMediator'
    viewClass = Ui_Form

    def __init__(self, mediatorName=None):
        super(MessageGroupWindowMediator, self).__init__(MessageGroupWindowMediator.NAME)
        self.log_done_thread = None
        self.LOG = logging.getLogger("MessageGroupWindowMediator")

    def onRegister(self):
        self.LOG.info("MessageGroupWindowMediator onRegister")
        self.log_done_thread = SignalThread()
        self.log_done_thread.signal.connect(self.refresh_log)

        self.getViewComponent().wxTextPushButton.clicked.connect(self.send_wx_text)
        # 这段代码解决了文本框回车发送的问题
        self.getViewComponent().wxTextEdit.installEventFilter(self)

    @permission_wcf
    def send_wx_text(self):
        txt = self.getViewComponent().wxTextEdit.toPlainText()
        if txt == "":
            return
        items = self.getSelectListWidget()
        if len(items) == 0:
            show_message("提示", "请先选择要发送的联系人")
            return
        self.getViewComponent().wxTextEdit.setText("")
        # 为了释放异步刷新界面的能力
        thread = threading.Thread(target=self.start_sendTXT, args=(txt,))
        thread.start()

    def start_sendTXT(self, txt):
        items = self.getSelectListWidget()
        if len(items) == 0:
            return False
        for item in items:
            if not WcfSSS.getInstance().is_running():
                break
            key = item.data(Qt.UserRole)
            vo = WxTextVO()
            vo.answer = txt
            vo.receiver = key
            self.sendNotification(Constant.SEND_WX_TEXT, vo)
            time.sleep(random.randint(2, 4))

            userName = item.text() + " 文本已发送！"
            # 为了释放异步刷新界面的能力
            self.log_done_thread.data = userName
            self.log_done_thread.start()
        self.LOG.info("文本信息群发完毕！")
        return True

    def refresh_log(self, text):
        self.getViewComponent().logPlainTextEdit.appendPlainText(text)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.getViewComponent().wxTextEdit:
            shift = False
            if event.modifiers() & Qt.ShiftModifier:
                shift = True
            if event.key() == Qt.Key_Return and self.getViewComponent().wxTextEdit.hasFocus():
                if shift:
                    self.getViewComponent().wxTextEdit.insertPlainText("")
                    return False
                self.send_wx_text()
                return True
        return False

    def onRemove(self):
        self.LOG.info("MessageGroupWindowMediator onRemove")
        pass

    def getViewComponent(self) -> Ui_Form:
        return super().getViewComponent()
