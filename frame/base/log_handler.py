#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import logging.config

"""
这个类是个单例，解决了UI对应mediator获取到日志，刷新到UI界面去
"""


class MyLogHandler(logging.Handler, object):
    """
    自定义日志handler
    """
    instance = None

    def __init__(self, name, other_attr=None, *args, **kwargs):
        logging.Handler.__init__(self)
        self.set_name(name)
        print('初始化自定义日志处理器：', name)
        print('其它属性值：', other_attr)

        # 自定义回调函数
        self.callbackFunc = None

    def emit(self, record):
        """
        emit函数为自定义handler类时必重写的函数，这里可以根据需要对日志消息做一些处理，比如发送日志到服务器

        发出记录(Emit a record)
        """
        try:
            msg = self.format(record)
            # print('获取到的消息为：', msg)
            if self.callbackFunc is not None:
                self.callbackFunc(msg)
            # for item in dir(record):
            #     if item in ['process', 'processName', 'thread', 'threadName']:
            #         print(item, '：', getattr(record, item))
        except Exception as e:
            # self.handleError(record)
            print(e)

    def __new__(cls, *args, **kwargs):
        if not cls.instance or not isinstance(cls.instance, cls):
            cls.instance = super(MyLogHandler, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def getInstance():
        return MyLogHandler.instance


if __name__ == '__main__':
    # 测试
    logging.basicConfig()
    logger = logging.getLogger("logger")
    logger.setLevel(logging.INFO)
    my_log_handler = MyLogHandler('LoggerHandler')
    logger.addHandler(my_log_handler)
    logger.info('hello，shouke')
