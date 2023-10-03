class WxDbContact:
    # wxid,房间id，示例：25596501119@chatroom，wxid_j1jew5sfz9jr11 等
    UserName: str = None
    # 昵称
    NickName: str = None
    # 备注名称
    Remark: str = None
    # 拼音
    PYInitial: str = None
    # 备注拼音
    RemarkPYInitial: str = None
    # 头像
    smallHeadImgUrl: str = None

    # 群里面非好友的类型为4, 未知类型是2
    Type: int = 0

    # 0非群内， 1 群内好友
    ChatRoomType: int = 0

    # 微信头像
    SmallHeadImgUrl: str = None
    # 用来判断是否是公众号或服务号的字段
    VerifyFlag: int = 0
