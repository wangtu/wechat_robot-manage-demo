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
答：
1、github release附件下载

2、访问天翼云盘
https://cloud.189.cn/t/ZFnqiq3Mjiqq （访问码：j8tj）

3、蓝奏云网盘，支持网页下载
https://wwyg.lanzouy.com/b052lfhmd
密码:cmok

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

开源版和专业版的区别

- 开源版：
  - 麻雀虽小五脏俱全！
  - 教学为主，包含完整架构
  - 不再维护更新
  - 微信版本：3.9.2.23
- 专业版：
  - 功能更加强大、稳定！
  - 支持长时间运行
  - 持续更新迭代
  - 微信版本：3.9.2.23



## [专业版，版本更新内容]

### [V1.5.0.1（2024.7.9）]
1、支持最新微信版本3.9.10.27


### [V1.5.0（2024.5.6）]
1、新增：消息转发模块，支持图片、文本转发，超骚
2、新增：自动回复新增指定微信通知，再也不错过关键信息了
3、新增：支持自定义知识库，结合大模型回复内容，你的专属客服
4、新增：自动回复新增复制功能，方便快速开新群复制模板回复
5、新增：消息群发模块新增支持卡片/公众号


### [V1.4.9 (2023.1.2)] 
1、新增：定时任务、自动回复支持卡片模式回复了，超强
2、新增：外部API支持图片返回了，可以发新闻图片了
3、新增：群邀请突破20人以上限制了，超级强
4、新增：定时活动新增-成语填空，好玩
5、新增：营销推广增加定时活动小尾巴
6、重构：邮件通知架构重构，适合办公人群
7、优化：对方拉黑，发送消息闪退修复
8、优化：关键字配置正则错误时软件闪退问题修复


### [v1.4.8 (2023.12.08)]

V1.4.8 微信办公助手，大版本更新啦！
1、新增：全局按功能区域配置营销小尾巴，营销轻松搞定
2、新增：自动回复图文、文件，定时回复的智能消息均支持同时配置自定义提示语
3、新增：联系人现在支持按微信标签筛选
4、新增：定时回复支持外部API调用，至于怎么玩就看你了
5、重构：定时回复-智能消息重构了毒鸡汤、侮辱人、段子手，内容更符合实际
6、优化：公众号侦听推广，高级角色支持一次批量选多个公众号
7、优化：优化界面加载顺序避免闪屏及其它运行稳定性优化



### [v1.4.6 (2023.11.24)]

微信办公助手v1.4.6 版本发布 
新增功能
1、新增公众号推广板块，收到公众号信息自动转发配置的群或好友
2、新增群管理-踢群白名单板块，再也不用担心误删群内小号啦
3、定时活动，签到活动支持修改关键字，这下可以实现早起,读书,运动,报名等等啦

优化功能
1、大量底层优化，加载快，性能更优，防日志资源锁住造成的假死优化等
2、自动回复支持带昵称回复了
3、自动回复支持过滤对象、关键字，再也不用担心数据太多管理困难啦
4、消息群发推送在途时，禁用群发控件，避免手误造成行为超出微信安全阈值
5、自动回复，如同一人或群内非@提问，命中关键词后，30s内相同且连续提问忽略，机器人装的没那么傻了

下载地址1-百度网盘链接：https://pan.baidu.com/s/1RTwCOIn7uIjfip2vnsAjzw?pwd=tutu 
提取码：tutu 

下载地址2-蓝奏云盘链接：https://wwyg.lanzouy.com/b052lfhmd
密码:cmok



### [v1.4.5 (2023.11.12)]

特大更新版本

1. 新增-定时活动板块，支持看图猜成语、签到功能，效果完美，暂限制黄铜及以上角色使用
2. 新增-免打扰设置：在设置的开始、结束将不会**触发定时回复、定时活动、邮件通知**所设置的间隔定时任务
3. 新增-留言反馈，功能使用过程有什么优化提议欢迎留言
4. 优化-智能AI回复新增律师角色，提供相关法律援助
5. 优化-现在支持在列表直接修改参数。包括自动回复、定时回复、群管理、邮件关键词和通知内容等（绿色标记）
6. 优化-现在群管理和自动回复，所设置的英文关键字自动忽略大小写，减少大量重复配置工作
7. 优化-高级角色，到期时间显示，即将到期前14天会主动提醒
8. 修复-群管理中配置多个群关键词踢人不生效修复、空格文本被发送出的问题修复等等



### [v1.4.4 (2023.11.5)]

1. 新增模块—屏蔽设置，是指对于你不感兴趣，或者无需关心的对象发来的消息，可将其添加到屏蔽列表中，那么之后此人发来的信息将不会命中[该机器人]的任何处理。群发自动屏蔽、关键字自动屏蔽、AI机器人自动回复屏蔽
2. 新增自动回复，支持音乐了，更多模式选择（输歌名/作者），或直接命中关键词直接发歌曲
3. 新增定时回复，智能消息支持，情人暧昧、侮辱、心灵鸡汤。
4. 群管理踢人设置增加网页链接、小程序监控，支持识别后自动踢人，踢人后自动发配置的踢人公告



### [v1.4.0 (2023.10.15)]

1、适配window全屏，优化列表
2、系统安全保护

重要：重要功能升级，10.17日后低于1.4.0版本的软件将无法登录，为保障您的权益请尽快下载新版本



### [v1.3.0 (2023.10.11)]

 1、新增群管理新人入群欢迎提示配置
 2、新增邮件通知，工作过程再也不会延误关键邮件了
 3、修改，关于调整为公告，实时获取最新信息
 4、定时回复增加智能AI能力，讲段子、团队打鸡血、国际新闻
 5、体验优化精简界面，新手操控界面更清爽 
 修复
 1、修复关键字选择群被人@不生效问题
 2、修复加群识别到关键字，再次回复AI消息
 3、修复主动删除好友后，主动发送消息死循环缺陷
 4、体验优化精简界面，新手操控界面更清爽
 5、启动成功通知，增加windows系统通知 3、压缩打包，文件更小

### [v1.0.3 (2023.10.7)]

fix：
1、修复关键字选择群被人@不生效问题
2、修复加群识别到关键字，再次回复AI消息
3、修复主动删除好友后，主动发送消息死循环缺陷
体验优化：
1、优化主界面交互设计，精简界面，新手操控界面更清爽
2、启动成功通知，增加windows系统通知
3、压缩打包，文件更小

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

### [v1.0.0 (2023.10.3)]

正式发布




| [<img src="assets/jqr.jpg" alt="加作者" style="zoom: 33%;" />](https://github.com/wangtu/wechat_robot-manage-demo/blob/main/assets/jqr.jpg) |
| ------------------------------------------------------------ |
| 加好友回复 `微信办公` 加群交流                               |
