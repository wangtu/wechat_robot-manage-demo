from builtins import list

from wcferry import Wcf, wcf_pb2

from frame.vo.wxdb_contact_vo import WxDbContact


class WcfSSS(Wcf):
    instance = None

    def __init__(self, host: str = None, port: int = 10086, debug: bool = True) -> None:
        super().__init__(host, port, debug)
        # 好友
        self.allFriends = []
        # 群聊
        self.chatRooms = []
        # 个人信息
        self.userInfo = {}

    def cleanup1(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.instance or not isinstance(cls.instance, cls):
            cls.instance = super(WcfSSS, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def getInstance():
        return WcfSSS.instance

    def __del__(self):
        super().__del__()

    def is_running(self) -> bool:
        return self._is_running

    def getAllContacts(self) -> dict:
        """
        慎重使用，数量量大后，卡慢
        获取联系人（包括好友、公众号、服务号、群成员……）
        格式: {"wxid": "NickName"}
        """
        contacts = self.query_sql("MicroMsg.db", "SELECT UserName, NickName FROM Contact;")
        return {contact["UserName"]: contact["NickName"] for contact in contacts}

    def getAllFriends(self) -> list:
        self.allFriends = []
        contacts = self.query_sql("MicroMsg.db",
                                  """
                                    SELECT
                                        UserName,Remark,NickName,PYInitial,RemarkPYInitial,t2.smallHeadImgUrl
                                    FROM
                                    Contact t1 LEFT JOIN ContactHeadImgUrl t2
                                    ON
                                        t1.UserName = t2.usrName
                                    WHERE
                                        t1.VerifyFlag = 0
                                    AND (t1.Type = 3 OR t1.Type > 50)
                                    AND t1.UserName NOT IN ("qmessage", "tmessage")
                                    ORDER BY
                                        t1.Remark DESC
                                  """)
        for contact in contacts:
            vo = WxDbContact()
            vo.UserName = contact["UserName"]
            vo.Remark = contact["Remark"]
            vo.NickName = contact["NickName"]
            vo.PYInitial = contact["PYInitial"]
            vo.RemarkPYInitial = contact["RemarkPYInitial"]
            vo.smallHeadImgUrl = contact["smallHeadImgUrl"]
            self.allFriends.append(vo)
        return self.allFriends

    def getAllChatRooms(self) -> list:
        self.chatRooms = []
        # t2.smallHeadImgUrl
        # LEFT JOIN ContactHeadImgUrl t2 ON t1.UserName = t2.usrName
        contacts = self.query_sql("MicroMsg.db",
                                  """
                                    SELECT
                                        UserName,
                                        Remark,
                                        NickName,
                                        PYInitial,
                                        RemarkPYInitial
                                    FROM
                                        Contact t1
                                    WHERE
                                        t1.Type = 2
                                  """)
        for contact in contacts:
            vo = WxDbContact()
            vo.UserName = contact["UserName"]
            vo.Remark = ""
            vo.NickName = contact["NickName"]
            vo.PYInitial = contact["PYInitial"]
            vo.RemarkPYInitial = ""
            # vo.smallHeadImgUrl = contact["smallHeadImgUrl"]
            self.chatRooms.append(vo)
        return self.chatRooms

    def getContact_NickName(self, wx_id) -> str:
        """
        获取联系人（包括好友、公众号、服务号、群成员……）
        """
        contacts = self.query_sql("MicroMsg.db", f"SELECT UserName, NickName FROM Contact WHERE UserName='{wx_id}';")
        if len(contacts) > 0:
            return contacts[0].get("NickName", "")
        return ""

    def getChatRoom_Name(self, wx_id, count=5) -> str:
        """
        如果群未添加名称，可调用该方法获取群成员姓名
        """
        if not wx_id:
            return ""
        result = ""
        roomNames = self.query_sql("MicroMsg.db", f"SELECT UserNameList FROM ChatRoom WHERE ChatRoomName = '{wx_id}';")
        userNameListStr = ""
        if len(roomNames) > 0:
            userNameList = roomNames[0].get("UserNameList", "")
            array = userNameList.split("^G")
            if len(array) > 2:
                array = array[1:count + 1]
                userNameListStr = ','.join(f"'{x}'" for x in array)

        if userNameListStr:
            contacts = self.query_sql("MicroMsg.db",
                                      f"SELECT Remark, NickName FROM Contact t1 WHERE t1.UserName in ({userNameListStr});")
            # [{'NickName': '军xx', 'Remark': '张xx'}, {'NickName': '斌xx', 'Remark': '陈xx'}]
            if len(contacts) > 0:
                for item in contacts:
                    result += item.get("Remark") if item.get("Remark") else item.get("NickName")
                    result += "、"

        return result

    def get_ChatRoom_User(self, wxid, roomid) -> str:
        """是否已经在群内, 如果命中，则同时也返回群内其它成员"""
        contacts = self.query_sql("MicroMsg.db",
                                  f"SELECT UserNameList FROM ChatRoom t1 WHERE t1.ChatRoomName = '{roomid}' AND t1.UserNameList LIKE '%{wxid}%';")
        if len(contacts) > 0:
            return contacts[0].get("UserNameList", "")
        return ""

    def init_user_info(self) -> dict:
        # {'wxid': 'wang****da', 'name': '图*', 'mobile': '180****7525', 'home': 'F:\\文档备份\\WeChat Files\\'}
        self.userInfo = super().get_user_info()
        return self.userInfo

    def send_xml(self, receiver: str, xml: str, type: int, path: str = None) -> int:
        """发送 XML

        Args:
            receiver (str): 消息接收人，wxid 或者 roomid
            xml (str): xml 内容
            type (int): xml 类型，如：0x21 为小程序
            path (str): 封面图片路径

        Returns:
            int: 0 为成功，其他失败
        """
        req = wcf_pb2.Request()
        req.func = wcf_pb2.FUNC_SEND_XML  # FUNC_SEND_XML
        req.xml.receiver = receiver
        req.xml.content = xml
        req.xml.type = type
        if path:
            req.xml.path = path
        rsp = self._send_request(req)
        return rsp.status


if __name__ == '__main__':
    wcf = WcfSSS(port=10086, debug=True)
    data = wcf.getContact("chen199508148")
    list = wcf.getAllFriends()
    print(list)
