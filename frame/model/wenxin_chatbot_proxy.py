import asyncio
import logging

from WenXinAPI.V1 import ChatBot
from frame.vo.chat_record_vo import ChatRecordVO
from util.sqlite_util import SqliteUtil

import puremvc.patterns.proxy
from util.dict_code_constant import DictCodeConstant

LOG = logging.getLogger("WeixinChatBotProxy.py")

# 文心一言的代理机器人，操控githubg 开源 V1对象
# 开源地址：https://github.com/umbrella-leaf/WenXinAPI/
""" 
该类的在本项目中，上游 由ai_user_proxy触发调度
本项目只处理发送逻辑
"""


class WeixinChatBotProxy(puremvc.patterns.proxy.Proxy):
    NAME = "WeixinChatBotProxy"

    def __init__(self, proxyName=None, data=None):
        super(WeixinChatBotProxy, self).__init__(WeixinChatBotProxy.NAME, [])
        self.default_chatbot: ChatBot = None
        self.self_chatbot: ChatBot = None
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self._config = None

        self.LOG = logging.getLogger("WeixinChatBotProxy")

    def init_default_robot(self):  # 初始化配置启动机器人
        # 初始化默认机器人
        if self.default_chatbot is None:
            key = "HaV80rXWTocBSqBkOX5viwlp"
            secret = "oDYwigVjY4oCgX9c3zDhEjLCnAxgtONX"
            self.default_chatbot = ChatBot(key, secret)
        else:
            self.default_chatbot.prompt_conversations = {}
            self.default_chatbot.last_ask_time = {}
            self.default_chatbot.conversations = {"default": []}

    def init_self_robot(self):  # 初始化自定义百度文心机器人
        # 初始化自定义百度文心机器人
        db = SqliteUtil.get_instance()
        key = db.query_dict_value(DictCodeConstant.WENXIN_ROBOT_KEY)
        secret = db.query_dict_value(DictCodeConstant.WENXIN_ROBOT_SECRET)
        if len(key.strip()) == 0 or len(secret.strip()) == 0:
            return
        if self.self_chatbot is None:
            self.self_chatbot = ChatBot(key, secret)
        else:
            self.self_chatbot.api_key = key
            self.self_chatbot.secret_key = secret
            self.self_chatbot.prompt_conversations = {}
            self.self_chatbot.last_ask_time = {}
            self.self_chatbot.conversations = {"default": []}

    def init_self_prompt(self, prompt: str, convo_id: str = "default"):
        if self.self_chatbot and prompt:
            self.self_chatbot.add_prompt(prompt, convo_id)

    def init_default_prompt(self, prompt: str, convo_id: str = "default"):
        if self.default_chatbot:
            self.default_chatbot.add_prompt(prompt, convo_id)

    def init_self_robot2(self, key, secret):  # 初始化自定义百度文心机器人
        # 初始化自定义百度文心机器人
        if self.self_chatbot is None:
            self.self_chatbot = ChatBot(key, secret)
        else:
            self.self_chatbot.api_key = key
            self.self_chatbot.secret_key = secret
            self.self_chatbot.prompt_conversations = {}
            self.self_chatbot.last_ask_time = {}
            self.self_chatbot.conversations = {"default": []}

    def default_ask(self, vo: any) -> str:
        return self._ask(self.default_chatbot, vo)

    def self_ask(self, vo: any) -> str:
        return self._ask(self.self_chatbot, vo)

    def _ask(self, chat: ChatBot, vo: any) -> str | None:
        if chat is None:
            return None

        def _sync_ask(question: str, convo_id: str = "default") -> str:
            try:
                task1 = self.loop.create_task(chat.ask(question, convo_id))

                self.loop.run_until_complete(task1)
                rsp = task1.result()
            except Exception:
                rsp = ""
            return rsp

        answer = ""
        if isinstance(vo, ChatRecordVO):
            if vo.wxmsg.from_group():
                answer = _sync_ask(vo.question, vo.wxmsg.roomid)
            else:
                answer = _sync_ask(vo.question, vo.wxmsg.sender)

        elif isinstance(vo, str):
            answer = _sync_ask(vo)

        return answer

    def onRemove(self):
        pass


if __name__ == '__main__':
    _proxy = WeixinChatBotProxy(None)
    _proxy.init_default_robot()
    print("_ask  start")

    # -------测试百度文心prompt提示词---------
    _proxy.init_self_robot2("HaV80rXWTocBSqBkOX5viwlp", "oDYwigVjY4oCgX9c3zDhEjLCnAxgtONX")
    _proxy.init_self_prompt("你将扮演名字叫做小白的IT技术人")
    _ask = _proxy.self_ask("你是谁")
    print(_ask)

    # _ask = _proxy.default_ask("我字的拼音是什么")
    # print(f"_ask  step 2 {_ask}")
    # _ask = _proxy.default_ask("你字的拼音是什么")
    # print(f"_ask  step 3 {_ask}")
    # _ask = _proxy.default_ask("他字的拼音是什么")
    # print(f"_ask  step 4 {_ask}")

    # while True:
    #     q = input(">>> ")
