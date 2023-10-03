import logging.config
import os

import yaml

import puremvc.patterns.proxy


def _load_config() -> dict:
    pwd = os.path.dirname(os.path.abspath(__file__))
    # 顶级目录
    pwd = os.path.abspath(pwd + os.path.sep + ".." + os.path.sep + "..")
    try:
        with open(f"{pwd}/config.yaml", "rb") as fp:
            yconfig = yaml.safe_load(fp)
    except FileNotFoundError:
        pass

    return yconfig


class ConfigProxy(puremvc.patterns.proxy.Proxy):
    NAME = "ConfigProxy"

    def __init__(self, proxyName=None, data=None):
        super(ConfigProxy, self).__init__(ConfigProxy.NAME, [])
        # self.EMAIL = None
        # self.WENXIN = None
        # self.NEWS = None
        # self.GROUPS = None
        # self.JOB = None
        self.reload()

    def reload(self) -> None:
        """
        初始化配置文件
        :return:
        """
        yconfig: dict = _load_config()
        logging.config.dictConfig(yconfig["logging"])
        # self.GROUPS = yconfig["groups"]["enable"]
        # self.NEWS = yconfig["news"]["receivers"]
        # self.WENXIN = yconfig.get("wenxin")
        # self.HELP = yconfig.get("monitor_help")
        # self.JOB = yconfig.get("job")
        # self.EMAIL = yconfig.get("email")


if __name__ == '__main__':
    cur_path = os.path.dirname(os.path.abspath(__file__))
    cur_path = os.path.abspath(cur_path + os.path.sep + ".." + os.path.sep + "..")
    print(cur_path)

    config = ConfigProxy(None)
    config.reload()
    print(config.GROUPS)
