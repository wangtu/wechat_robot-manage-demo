import logging
import re
import threading
import xml.etree.ElementTree as ET
from queue import Empty

from wcferry import Wcf, WxMsg

import puremvc.interfaces
import puremvc.patterns.mediator
from frame.base.wcf_sss import WcfSSS
from frame.constant import Constant
from frame.model.config_proxy import ConfigProxy
from frame.vo.wx_text_vo import WxTextVO
from puremvc.patterns.observer import Notification


# 机器人控制层，启动注入dll，拦截手发操控微信客户端
# wechat控制指令参考，https://github.com/lich0821/WeChatRobot
# 微信注入、拦截、伪装、控制参考，https://github.com/lich0821/WeChatFerry
# WeChatFerry: 一个玩微信的工具，参考 https://mp.weixin.qq.com/s/CGLfSaNDy8MyuyPWGjGJ7w
class WcfMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):
    NAME = 'WcfMediator'

    def __init__(self, viewComponent=None):
        super(WcfMediator, self).__init__(WcfMediator.NAME, viewComponent)
        self.USER_INFO = None
        self.WX_ID = None
        self.wcf: WcfSSS = None
        self.LOG = logging.getLogger("WcfMediator")

        self.sayHelloProxy = None

    def onRegister(self):
        print("WcfMediator onRegister")

    def listNotificationInterests(self):
        return [
            Constant.SEND_WX_TEXT,
            Constant.EXIT,
            Constant.START_WCF,
            Constant.STOP_WCF,
        ]

    def handleNotification(self, notification: Notification):
        notName = notification.getName()
        vo = notification.getBody()
        if notName == Constant.EXIT:
            self.onRemove()
        elif notName == Constant.START_WCF:
            # 为了释放异步刷新界面的能力
            thread = threading.Thread(target=self.start_wcf)
            thread.start()
        elif notName == Constant.STOP_WCF:
            # 为了释放异步刷新界面的能力
            thread = threading.Thread(target=self.stop_wcf)
            thread.start()
        elif notName == Constant.SEND_WX_TEXT:
            if isinstance(vo, WxTextVO) and vo.answer:
                self.sendTextMsg(vo.answer, vo.receiver, vo.at_list)

    def start_wcf(self):
        self.LOG.info("正在启动机器人...")
        self.wcf = WcfSSS(port=Constant.WCF_PORT, debug=True)
        self.LOG.info("机器人启动成功！")
        if self.wcf.is_running():
            self.LOG.info("正在读取联系人信息...")
            self.wcf.getAllChatRooms()
            self.wcf.getAllFriends()
            self.LOG.info("联系人信息读取成功")
            self.LOG.info("正在读取登录信息...")

            self.USER_INFO = self.wcf.init_user_info()
            self.WX_ID = self.USER_INFO.get("wxid")
            print(self.USER_INFO)
            self.LOG.info(f"读取登录信息成功{self.WX_ID}")
            self.sendNotification(Constant.START_WCF_SUCCESS, self.wcf)
            # 侦听消息
            self.enableReceivingMsg()

    def stop_wcf(self):
        if self.wcf is None:
            self.LOG.info("机器人wcf尚未启动")
            return

        self.LOG.info("正在关闭机器人wcf...")
        self.wcf.cleanup()  # 退出前清理环境
        self.LOG.info("机器人退出成功！!")
        self.sendNotification(Constant.STOP_WCF_SUCCESS)

    def __getConfig(self) -> ConfigProxy:
        if self.config is not None:
            return self.config
        else:
            _config: ConfigProxy = self.facade.retrieveProxy(ConfigProxy.NAME)
            if _config is not None:
                self.config = _config
            return self.config

    def sendTextMsg(self, msg: str, receiver: str, at_list: str = "") -> None:
        """ 发送消息
        :param msg: 消息字符串
        :param receiver: 接收人wxid或者群id
        :param at_list: 要@的wxid, @所有人的wxid为：notify@all
        """
        # msg 中需要有 @ 名单中一样数量的 @
        ats = ""
        if at_list:
            if at_list == "notify@all":
                ats = "notify@all"
            else:
                wx_ids = at_list.split(",")
                for wx_id in wx_ids:
                    # 这里偷个懒，直接 @昵称。有必要的话可以通过 MicroMsg.db 里的 ChatRoom 表，解析群昵称
                    ats += f" @{self.wcf.getContact_NickName(wx_id)}"

        # {msg}{ats} 表示要发送的消息内容后面紧跟@，例如 北京天气情况为：xxx @张三，微信规定需这样写，否则@不生效
        if ats == "":
            self.LOG.info(f"To {receiver}: {msg}")
            self.wcf.send_text(f"{msg}", receiver, at_list)
        else:
            self.LOG.info(f"To {receiver}: {ats}\r{msg}")
            self.wcf.send_text(f"{ats} {msg}", receiver, at_list)

    def enableReceivingMsg(self) -> None:
        def innerProcessMsg(wcf: Wcf):
            while wcf.is_receiving_msg():
                try:
                    msg = wcf.get_msg()
                    if msg.from_group():
                        self.LOG.info(msg.roomid + ": " + msg.content)
                    else:
                        self.LOG.info(msg.sender + ": " + msg.content)
                    self.processMsg(msg)
                except Empty:
                    continue  # Empty message
                except Exception as e:
                    self.LOG.error(f"Receiving message error: {e}")

        self.wcf.enable_receiving_msg()
        threading.Thread(target=innerProcessMsg, name="GetMessage", args=(self.wcf,), daemon=True).start()

    def processMsg(self, msg: WxMsg) -> None:
        """当接收到消息的时候，会调用本方法。如果不实现本方法，则打印原始消息。
        此处可进行自定义发送的内容,如通过 msg.content 关键字自动获取当前天气信息，并发送到对应的群组@发送者
        群号：msg.roomid  微信ID：msg.sender  消息内容：msg.content
        content = "xx天气信息为："
        receivers = msg.roomid
        self.sendTextMsg(content, receivers, msg.sender)
        """
        # 非群聊信息，按消息类型进行处理
        print(msg.type, msg.from_group(), msg.sender)
        if msg.type == 37:  # 好友请求
            pass
        elif msg.type == 10000:  # 系统信息
            # self.sayHiToNewFriend(msg)
            pass
        elif msg.type == 0x01:  # 文本消息
            # 让配置加载更灵活，自己可以更新配置。也可以利用定时任务更新。
            # 自己发的文本消息，可以作命令控制后台
            if msg.from_self():
                pass
            else:
                question = re.sub(r"@.*?[\u2005|\s]", "", msg.content).replace(" ", "")
                msg.content = question
                self.LOG.info(msg.sender + ": " + msg.content)

    def autoAcceptFriendRequest(self, msg: WxMsg) -> None:
        # 自动添加好友
        try:
            xml = ET.fromstring(msg.content)
            v3 = xml.attrib["encryptusername"]
            v4 = xml.attrib["ticket"]
            scene = int(xml.attrib["scene"])
            self.wcf.accept_new_friend(v3, v4, scene)

        except Exception as e:
            self.LOG.error(f"同意好友出错：{e}")

    def onRemove(self):
        self.LOG.info("关闭机器人wcf机器")
        if self.wcf is not None:
            self.wcf.cleanup()  # 退出前清理环境
