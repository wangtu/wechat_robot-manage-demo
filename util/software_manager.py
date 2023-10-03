import re
import winreg


class SoftwareManager:
    def __init__(self):
        self.sub_keys = [
            r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
            r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall'
        ]
        self.__installed = self.__load_all_installed()

    def __get_value(self, each_key, name):
        try:
            value = winreg.QueryValueEx(each_key, name)[0]
        except Exception:
            value = None
        return value

    def __load_all_installed(self):
        installed = []
        for sub_key in self.sub_keys:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub_key) as sub_key_handle:
                for i in range(winreg.QueryInfoKey(sub_key_handle)[0]):
                    try:
                        each_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                                  f'{sub_key}\\{winreg.EnumKey(sub_key_handle, i)}')
                    except Exception as e:
                        ...
                    else:
                        DisplayName = self.__get_value(each_key, "DisplayName")
                        if not DisplayName:
                            continue
                        installed.append({
                            "DisplayName": DisplayName,
                            "DisplayVersion": self.__get_value(each_key, "DisplayVersion"),
                            "DisplayIcon": self.__get_value(each_key, "DisplayIcon"),
                            "InstallDate": self.__get_value(each_key, "InstallDate"),
                            "InstallLocation": self.__get_value(each_key, "InstallLocation"),
                            "Publisher": self.__get_value(each_key, "Publisher"),
                        })
                    finally:
                        each_key.Close()
        return installed

    def get_all(self):
        """
        获取所有安装列表
        :return:
        """
        return self.__installed

    def get_by_name(self, name):
        """
        通过名字查找已安装软件
        :param name:
        :return:
        """
        one = [i for i in self.__installed if i.get('DisplayName') == name]
        return one[0] if one else None

    def re_search(self, pattern, flags=0):
        """
        通过正则搜索匹配项
        :param pattern:
        :param flags:
        :return:
        """
        return [i for i in self.__installed if re.search(pattern=pattern, string=i.get('DisplayName', ''), flags=flags)]


if __name__ == '__main__':
    manager = SoftwareManager()

    # 通过名字获取
    wechat = manager.get_by_name("微信")
    print(
        wechat['DisplayName'],  # 软件名
        wechat['DisplayVersion'],  # 软件版本
        wechat['InstallLocation'],  # 软件安装路径
    )
