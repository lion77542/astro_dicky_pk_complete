"""
Astro Dicky PK - Complete Edition
牛子 PK 完整版 - AstrBot 标准化插件

严格按照 AstrBot Skills 规范开发
"""

import logging
from astrbot.api import AstrBotConfig
from astrbot.api.event import AstrMessageEvent
from astrbot.api.event import filter
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import At

logger = logging.getLogger("astrbot")


@register(
    "astro_dicky_pk_complete",
    "tkgs0 (原), lion77542 (移植)",
    "🎮 完整保留原版所有功能的牛子 PK 游戏",
    "v3.0.1",
    "https://github.com/lion77542/astro_dicky_pk_complete"
)
class DickyPKPlugin(Star):
    """牛子 PK 完整版插件"""

    def __init__(self, context: Context, config: AstrBotConfig) -> None:
        super().__init__(context)
        self.config = config
        self.initialized = False
        logger.info("🎮 Astro Dicky PK - Complete Edition v3.0.1 加载中...")

    async def initialize(self):
        """初始化插件 - AstrBot 会自动调用"""
        if not self.initialized:
            # 初始化数据库
            from .src.db import Sql
            Sql.init_database()
            
            # 检查配置
            from .src.config import Config
            Config.deprecated_tips()
            
            self.initialized = True
            logger.info("✅ 插件初始化完成")

    def _get_sender_id(self, event: AstrMessageEvent) -> str:
        """获取发送者 ID"""
        return str(event.get_sender_id())

    def _get_sender_name(self, event: AstrMessageEvent) -> str:
        """获取发送者昵称"""
        return event.get_sender_name() or "未知用户"

    def _get_group_id(self, event: AstrMessageEvent) -> int:
        """获取群组 ID"""
        if hasattr(event.message_obj, 'group_id'):
            return event.message_obj.group_id or 0
        return 0

    def _get_at_qq(self, event: AstrMessageEvent) -> int | None:
        """获取被@的用户 ID"""
        for comp in event.message_obj.message:
            if isinstance(comp, At):
                return int(comp.qq)
        return None

    def _process_message(self, event: AstrMessageEvent, message: str, require_at: bool = False) -> str | None:
        """处理消息并返回结果"""
        sender_id = self._get_sender_id(event)
        sender_name = self._get_sender_name(event)
        group_id = self._get_group_id(event)
        at_qq = self._get_at_qq(event)

        if require_at and not at_qq:
            return "请@你想操作的人！"

        # 收集消息的列表
        collected_messages = []
        
        # 创建消息发送钩子
        def send_message_hook(qq, group, message):
            if isinstance(message, str):
                collected_messages.append(message)
            elif isinstance(message, list):
                collected_messages.extend([m for m in message if m])

        # 调用原项目的 message_processor
        from .src.main import message_processor
        result = message_processor(
            message=message,
            qq=int(sender_id),
            group=group_id,
            at_qq=at_qq,
            nickname=sender_name,
            impl_send_message=send_message_hook
        )

        # 返回收集到的消息
        if collected_messages:
            return "\n".join(collected_messages)
        elif result:
            return str(result)
        return None

    @filter.command("牛子帮助")
    @filter.command("帮助")
    async def cmd_help(self, event: AstrMessageEvent):
        """显示帮助信息"""
        from .src.main import HELPPER
        yield event.plain_result(HELPPER)

    @filter.command("注册牛子")
    async def cmd_sign_up(self, event: AstrMessageEvent):
        """注册牛子"""
        result = self._process_message(event, "注册牛子")
        if result:
            yield event.plain_result(result)

    @filter.command("牛子")
    async def cmd_chinchin(self, event: AstrMessageEvent):
        """查看牛子信息"""
        result = self._process_message(event, "牛子")
        if result:
            yield event.plain_result(result)

    @filter.command("牛子排名")
    @filter.command("排行")
    async def cmd_ranking(self, event: AstrMessageEvent):
        """查看排名"""
        result = self._process_message(event, "牛子排名")
        if result:
            yield event.plain_result(result)

    @filter.command("牛子成就")
    async def cmd_badge(self, event: AstrMessageEvent):
        """查看成就"""
        result = self._process_message(event, "牛子成就")
        if result:
            yield event.plain_result(result)

    @filter.command("牛子转生")
    async def cmd_rebirth(self, event: AstrMessageEvent):
        """转生"""
        result = self._process_message(event, "牛子转生")
        if result:
            yield event.plain_result(result)

    @filter.command("牛子仙境")
    async def cmd_farm_info(self, event: AstrMessageEvent):
        """查看农场"""
        result = self._process_message(event, "牛子仙境")
        if result:
            yield event.plain_result(result)

    @filter.command("牛子修炼")
    @filter.command("牛子练功")
    @filter.command("牛子修仙")
    async def cmd_farm_start(self, event: AstrMessageEvent):
        """开始修炼"""
        result = self._process_message(event, "牛子修炼")
        if result:
            yield event.plain_result(result)

    @filter.command("牛友")
    @filter.command("牛子好友")
    async def cmd_friends(self, event: AstrMessageEvent):
        """查看好友"""
        result = self._process_message(event, "牛友")
        if result:
            yield event.plain_result(result)

    @filter.command("🔒我")
    @filter.command("锁我")
    async def cmd_lock_me(self, event: AstrMessageEvent):
        """锁自己"""
        result = self._process_message(event, "🔒我")
        if result:
            yield event.plain_result(result)

    @filter.command("打胶")
    async def cmd_glue(self, event: AstrMessageEvent):
        """打胶"""
        result = self._process_message(event, "打胶")
        if result:
            yield event.plain_result(result)

    @filter.command("pk")
    async def cmd_pk(self, event: AstrMessageEvent):
        """PK"""
        result = self._process_message(event, "pk", require_at=True)
        if result:
            yield event.plain_result(result)

    @filter.command("看他牛子")
    @filter.command("看看牛子")
    async def cmd_see_chinchin(self, event: AstrMessageEvent):
        """查看别人的牛子"""
        result = self._process_message(event, "看他牛子", require_at=True)
        if result:
            yield event.plain_result(result)

    @filter.command("添加牛友")
    @filter.command("添加朋友")
    async def cmd_friends_add(self, event: AstrMessageEvent):
        """添加好友"""
        result = self._process_message(event, "添加牛友", require_at=True)
        if result:
            yield event.plain_result(result)

    @filter.command("删除牛友")
    @filter.command("删除朋友")
    async def cmd_friends_delete(self, event: AstrMessageEvent):
        """删除好友"""
        result = self._process_message(event, "删除牛友", require_at=True)
        if result:
            yield event.plain_result(result)

    @filter.command("🔒")
    @filter.command("锁")
    async def cmd_lock_target(self, event: AstrMessageEvent):
        """锁别人"""
        result = self._process_message(event, "🔒", require_at=True)
        if result:
            yield event.plain_result(result)

    async def terminate(self):
        """插件卸载时清理"""
        logger.info("⏹️ Astro Dicky PK 已停止")
