class Constant:
    WCF_PORT = 10086
    WECHAT_VERSION = "3.9.2.23"
    VERSION = "V1.0"

    # 退出指令，回收各种系统参数，无需传参
    EXIT: str = "exit"

    SEND_WX_TEXT: str = "sendWxText"

    # 唤起新模块
    # 传递参数 from frame.vo.module_vo import ModuleVO
    SWITCH_QWIDGET: str = "switch_QWidget"
    # 传递参数 self, 继承BaseQWidgetMediator
    CLOSE_QWIDGET: str = "close_QWidget"

    # 删除子类，传递数组继承BaseQWidgetMediator,[baseMediator1,baseMediator2]
    CLOSE_CHILD_QWIDGET: str = "close_child_QWidget"

    START_WCF: str = "startWCF"

    START_WCF_SUCCESS: str = "startWCFSuccess"

    STOP_WCF: str = "stopWCF"

    STOP_WCF_SUCCESS: str = "stopWCFSuccess"

    # 获取角色权限成功后，刷新主界面数据
    UPDATE_USER_VIEW: str = "updateUserView"

    UPDATE_USER_VIEW_MESSAGE_COUNT: str = "updateUserView_message_count"

    UPDATE_USER_VIEW_KEY_COUNT: str = "updateUserView_key_count"

    # 发出html截图指令
    # 传递参数 from frame.vo.html2img_vo import Html2ImgVO
    HTML2IMG_START: str = "html2img_start"

    # 完成截图指令
    # 传递参数 from frame.vo.html2img_vo import Html2ImgVO
    HTML2IMG_START_COMPLETE: str = "html2img_complete"
