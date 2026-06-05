"""
Astro Dicky PK - Complete Edition
牛子 PK 完整版 - AstrBot 标准化插件

✨ Full port with ALL original features preserved!
✅ Compatible with AstrBot >= 4.16
🎮 Supports: QQ/Telegram/Discord/Lark
"""

import logging
from astrbot.api import AstrBotConfig
from astrbot.api.event import AstrMessageEvent
from astrbot.api.event import filter
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import At

from .src.main import message_processor, KEYWORDS, VERSION, HELPPER

logger = logging.getLogger("astrbot")


@register(
    "astro_dicky_pk_complete",
    "tkgs0 (原), lion77542 (移植)",
    "🎮 完整保留原版所有功能的牛子 PK 游戏",
    "v2.0.0",
    "https://github.com/lion77542/astro_dicky_pk_complete"
)
class DickyPKPlugin(Star):
    """牛子 PK 完整版插件"""

    def __init__(self, context: Context, config: AstrBotConfig) -> None:
        super().__init__(context)
        self.config = config
        logger.info(f"🎮 Astro Dicky PK - Complete Edition v{VERSION} 加载中...")

    def _get_sender_info(self, event: AstrMessageEvent):
        """获取发送者信息"""
        sender_id = event.get_sender_id()
        sender_name = event.get_sender_name()
        group_id = ""
        if hasattr(event, 'get_group_id'):
            group_id = event.get_group_id()
        elif hasattr(event, 'message_obj') and hasattr(event.message_obj, 'group_id'):
            group_id = event.message_obj.group_id
        return str(sender_id), sender_name, str(group_id)

    def _get_at_qq(self, event: AstrMessageEvent):
        """获取被@的用户ID"""
        for comp in event.message_obj.message:
            if isinstance(comp, At):
                return str(comp.qq)
        return None

    def _process_message(self, event: AstrMessageEvent, message: str, require_at: bool = False):
        """统一处理消息"""
        sender_id, sender_name, group_id = self._get_sender_info(event)
        at_qq = self._get_at_qq(event)

        if require_at and not at_qq:
            return event.plain_result("请@你想操作的人！")

        result = message_processor(
            message=message,
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            at_qq=int(at_qq) if at_qq else None,
            nickname=sender_name
        )

        if result:
            return event.plain_result(result)
        return None

    @filter.command("牛子帮助")
    @filter.command("帮助")
    async def cmd_help(self, event: AstrMessageEvent):
        """显示帮助信息"""
        yield event.plain_result(HELPPER)

    @filter.command("注册牛子")
    async def cmd_sign_up(self, event: AstrMessageEvent):
        """注册牛子"""
        result = self._process_message(event, "注册牛子")
        if result:
            yield result

    @filter.command("牛子")
    async def cmd_chinchin(self, event: AstrMessageEvent):
        """查看牛子信息"""
        result = self._process_message(event, "牛子")
        if result:
            yield result

    @filter.command("牛子排名")
    @filter.command("排行")
    async def cmd_ranking(self, event: AstrMessageEvent):
        """查看排名"""
        result = self._process_message(event, "牛子排名")
        if result:
            yield result

    @filter.command("牛子成就")
    async def cmd_badge(self, event: AstrMessageEvent):
        """查看成就"""
        result = self._process_message(event, "牛子成就")
        if result:
            yield result

    @filter.command("牛子转生")
    async def cmd_rebirth(self, event: AstrMessageEvent):
        """转生"""
        result = self._process_message(event, "牛子转生")
        if result:
            yield result

    @filter.command("牛子仙境")
    async def cmd_farm_info(self, event: AstrMessageEvent):
        """查看农场"""
        result = self._process_message(event, "牛子仙境")
        if result:
            yield result

    @filter.command("牛子修炼")
    @filter.command("牛子练功")
    @filter.command("牛子修仙")
    async def cmd_farm_start(self, event: AstrMessageEvent):
        """开始修炼"""
        result = self._process_message(event, "牛子修炼")
        if result:
            yield result

    @filter.command("牛友")
    @filter.command("牛子好友")
    async def cmd_friends(self, event: AstrMessageEvent):
        """查看好友"""
        result = self._process_message(event, "牛友")
        if result:
            yield result

    @filter.command("🔒我")
    @filter.command("锁我")
    async def cmd_lock_me(self, event: AstrMessageEvent):
        """锁自己"""
        result = self._process_message(event, "🔒我")
        if result:
            yield result

    @filter.command("打胶")
    async def cmd_glue(self, event: AstrMessageEvent):
        """打胶"""
        result = self._process_message(event, "打胶")
        if result:
            yield result

    @filter.command("pk")
    async def cmd_pk(self, event: AstrMessageEvent):
        """PK"""
        result = self._process_message(event, "pk", require_at=True)
        if result:
            yield result

    @filter.command("看他牛子")
    @filter.command("看看牛子")
    async def cmd_see_chinchin(self, event: AstrMessageEvent):
        """查看别人的牛子"""
        result = self._process_message(event, "看他牛子", require_at=True)
        if result:
            yield result

    @filter.command("添加牛友")
    @filter.command("添加朋友")
    async def cmd_friends_add(self, event: AstrMessageEvent):
        """添加好友"""
        result = self._process_message(event, "添加牛友", require_at=True)
        if result:
            yield result

    @filter.command("删除牛友")
    @filter.command("删除朋友")
    async def cmd_friends_delete(self, event: AstrMessageEvent):
        """删除好友"""
        result = self._process_message(event, "删除牛友", require_at=True)
        if result:
            yield result

    @filter.command("🔒")
    @filter.command("锁")
    async def cmd_lock_target(self, event: AstrMessageEvent):
        """锁别人"""
        result = self._process_message(event, "🔒", require_at=True)
        if result:
            yield result

    async def terminate(self):
        """插件卸载时清理"""
        logger.info("⏹️ Astro Dicky PK 已停止")
