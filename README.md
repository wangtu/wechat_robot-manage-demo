# wechat_robot-manage-demo

微信办公助手是一款强大的集人工智能技术与微信整合的管理软件，自动回复软件，客服软件，人工智能技术驱动的自然语言处理工具，同时具备其他高效功能，一切功能尽可能模拟人工操作，从而提高工作效率，同时让更多人低门槛接触人工智能帮助学习、办公等应用场景。更多介绍见：[微信办公助手帮助手册](https://k23x0697eg.feishu.cn/docx/LpdSdSVQ1oBVi4xVZ8lccBi9nYn)



**免责声明：**

- 本工具仅供学习和技术研究使用，不得用于任何商业或非法行为，否则后果自负。

- 本工具的作者不对本工具的安全性、完整性、可靠性、有效性、正确性或适用性做任何明示或暗示的保证，也不对本工具的使用或滥用造成的任何直接或间接的损失、责任、索赔、要求或诉讼承担任何责任。

- 本工具的作者保留随时修改、更新、删除或终止本工具的权利，无需事先通知或承担任何义务。

- 本工具的使用者应遵守相关法律法规，尊重微信的版权和隐私，不得侵犯微信或其他第三方的合法权益，不得从事任何违法或不道德的行为。

- 本工具的使用者在下载、安装、运行或使用本工具时，即表示已阅读并同意本免责声明。如有异议，请立即停止使用本工具，并删除所有相关文件。


核心框架主要采用开源**WechatFerry**、**PureMVC**、**PyQT5**

更多介绍见：
[WeChatFerry: 一个玩微信的工具](https://mp.weixin.qq.com/s/CGLfSaNDy8MyuyPWGjGJ7w)。

[PureMVC:一个支持18语言的轻量](https://github.com/PureMVC)。

[PyQT5::一个Python图形界面开发库](https://github.com/PyQT5)





## [完整项目]

更多介绍见：[微信办公助手帮助手册](https://k23x0697eg.feishu.cn/docx/LpdSdSVQ1oBVi4xVZ8lccBi9nYn)

```
要花钱吗？
答：免费的，重要的事情说三遍，免费！免费！免费！不用钱，香不香?

怎么试用？
答：下载软件，启动页选择①启动办公，弹出微信登录窗口，选择登录即可，每天默认每个vx角色都会发新的额度（群发、AI聊天）

下载地址？
答：github release附件下载
或访问百度网盘，关注最新版本发布
链接：https://pan.baidu.com/s/1RTwCOIn7uIjfip2vnsAjzw?pwd=tutu 
提取码：tutu 
```

## [开源项目结构]

```
为什么开源？
答：开源的初衷是本着授人以鱼不如授人以渔，Pyqt5的教程很少，完整应用复杂工程几乎很难找到比较满意的，基于pureMVC做封装和实现，简化了示例调用的门槛。

该项目有点是什么？
答：界面UI编程更简单
如两行代码可以唤起一个自定义好的弹窗
module: ModuleVO = ModuleVO(MainWindowMediator)
self.sendNotification(Constant.SWITCH_QWIDGET, module)


开源和完整项目有什么差异？
答：开源100%完全相同的核心框架和UI（仅实现屏蔽，该开源项目直接编码自己定义实现的）。方便更多的人技术学习交流。
具备部分完整功能（软件检测、环境检测、文本消息群发、MVC架构的UI编程）方便学习理解


wechat_robot-manage-demo
├── LICENSE                 # LICENSE
├── README.MD               # 说明
├── puremvc
│   ├── core.py     		# 核心框架有点缺陷，fix修复
│   ├── interfaces.py       # 框架源码
├── frame
│   ├── base             	# 包含框架核心工具UI异步刷新、wcf
│   ├── model         		# 代理类，实现自动界面加载、隐藏逻辑
│   ├── view  				# 对wcf做控制
│   └── vo            		# mvc交互中传递的对象
├── yyd
│   ├── aop                 # 切面编程，通过注解判断wcf是否已启动
│   ├── child               # main窗口的各tab子界面
│   ├── screen              # 主界面分别是首页和主题窗口两个界面
├── util
│   ├── common_util.py      # 异步刷新弹窗
│   └── software_manager    # 软件版本检测
└── wcferry                 # 一个玩微信的工具包
└── main.py                 # 启动函数
```



## [版本更新]

### [v1.0.0 (2023.10.3)]

正式发布

### [v1.0.1 (2023.10.5)]
修复相关问题：
1、增加空内容文本回复提示
2、修复允许昵称为空的微信用户也能使用
3、自动添加拉群时，欢迎语延迟2秒，避免加群者收不到
4、修复删除操作联系人时，误删多人
5、修复当天首次登录不显示群发、AI额度的缺陷
优化：
1、界面精简，优化提示
2、删除操控面板的操作联系人，更灵敏

### [v1.0.3 (2023.10.7)]
fix：
1、修复关键字选择群被人@不生效问题
2、修复加群识别到关键字，再次回复AI消息
3、修复主动删除好友后，主动发送消息死循环缺陷
体验优化：
1、优化主界面交互设计，精简界面，新手操控界面更清爽
2、启动成功通知，增加windows系统通知
3、压缩打包，文件更小


| [![碲矿](https://github.com/lich0821/WeChatFerry/raw/master/assets/TEQuant.jpg)](https://github.com/lich0821/WeChatFerry/blob/master/assets/TEQuant.jpg) | [<img src="assets/QR.png" alt="加作者" style="zoom: 55%;" />](https://github.com/lich0821/WeChatFerry/blob/master/assets/QR.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 回复`WeChatFerry` 加群交流                                   | 加作者交流                                                   |
