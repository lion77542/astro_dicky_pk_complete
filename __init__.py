"""
Astro Dicky PK - Complete Edition
牛子 PK 完整版 - AstrBot 标准化插件

✨ Full port with ALL original features preserved!
✅ Compatible with AstrBot >= 4.16
🎮 Supports: QQ/Telegram/Discord/Lark
"""

from astrbot.api import logger
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import Plain, At

from .src.main import message_processor, KEYWORDS, VERSION, HELPPER
from .src.db import lazy_init_database


@register(
    "astro_dicky_pk_complete", 
    "tkgs0 (原), lion77542 (移植)", 
    "🎮 完整保留原版所有功能的牛子 PK 游戏",
    "v2.0.0",
    "https://github.com/lion77542/astro_dicky_pk_complete"
)
class AstroDickyPK(Star):
    """牛子 PK 完整版插件"""

    def __init__(self, context: Context, config: dict):
        super().__init__(context, config)
        self.initialized = False
        logger.info(f"🎮 Astro Dicky PK - Complete Edition v{VERSION} 加载中...")

    async def initialize(self):
        """插件初始化"""
        if not self.initialized:
            await lazy_init_database()
            self.initialized = True
            logger.info("✅ 数据库初始化完成")

    def _get_sender_info(self, event: AstrMessageEvent):
        """获取发送者信息"""
        sender_id = event.get_sender_id()
        sender_name = event.get_sender_name()
        group_id = ""
        
        # 尝试获取群组ID
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

    def _get_text_content(self, event: AstrMessageEvent):
        """获取文本内容"""
        text_parts = []
        for comp in event.message_obj.message:
            if isinstance(comp, Plain):
                text_parts.append(comp.text)
        return "".join(text_parts).strip()

    @filter.command("牛子帮助")
    @filter.command("帮助")
    async def cmd_help(self, event: AstrMessageEvent):
        """显示帮助信息"""
        yield event.plain_result(HELPPER)

    @filter.command("注册牛子")
    async def cmd_sign_up(self, event: AstrMessageEvent):
        """注册牛子"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        result = message_processor(
            message="注册牛子",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("牛子")
    async def cmd_chinchin(self, event: AstrMessageEvent):
        """查看牛子信息"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        result = message_processor(
            message="牛子",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("牛子排名")
    @filter.command("排行")
    async def cmd_ranking(self, event: AstrMessageEvent):
        """查看排名"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        result = message_processor(
            message="牛子排名",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("牛子成就")
    async def cmd_badge(self, event: AstrMessageEvent):
        """查看成就"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        result = message_processor(
            message="牛子成就",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("牛子转生")
    async def cmd_rebirth(self, event: AstrMessageEvent):
        """转生"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        result = message_processor(
            message="牛子转生",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("牛子仙境")
    async def cmd_farm_info(self, event: AstrMessageEvent):
        """查看农场"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        result = message_processor(
            message="牛子仙境",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("牛子修炼")
    @filter.command("牛子练功")
    @filter.command("牛子修仙")
    async def cmd_farm_start(self, event: AstrMessageEvent):
        """开始修炼"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        result = message_processor(
            message="牛子修炼",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("牛友")
    @filter.command("牛子好友")
    async def cmd_friends(self, event: AstrMessageEvent):
        """查看好友"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        result = message_processor(
            message="牛友",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("🔒我")
    @filter.command("锁我")
    async def cmd_lock_me(self, event: AstrMessageEvent):
        """锁自己"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        result = message_processor(
            message="🔒我",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("打胶")
    async def cmd_glue(self, event: AstrMessageEvent):
        """打胶"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        # 检查是否有@目标
        at_qq = self._get_at_qq(event)
        
        result = message_processor(
            message="打胶",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            at_qq=int(at_qq) if at_qq else None,
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("pk")
    async def cmd_pk(self, event: AstrMessageEvent):
        """PK"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        # PK必须有@目标
        at_qq = self._get_at_qq(event)
        if not at_qq:
            yield event.plain_result("请@你想PK的人！")
            return
        
        result = message_processor(
            message="pk",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            at_qq=int(at_qq),
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("看他牛子")
    @filter.command("看看牛子")
    async def cmd_see_chinchin(self, event: AstrMessageEvent):
        """查看别人的牛子"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        at_qq = self._get_at_qq(event)
        if not at_qq:
            yield event.plain_result("请@你想查看的人！")
            return
        
        result = message_processor(
            message="看他牛子",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            at_qq=int(at_qq),
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("添加牛友")
    @filter.command("添加朋友")
    async def cmd_friends_add(self, event: AstrMessageEvent):
        """添加好友"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        at_qq = self._get_at_qq(event)
        if not at_qq:
            yield event.plain_result("请@你想添加的好友！")
            return
        
        result = message_processor(
            message="添加牛友",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            at_qq=int(at_qq),
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("删除牛友")
    @filter.command("删除朋友")
    async def cmd_friends_delete(self, event: AstrMessageEvent):
        """删除好友"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        at_qq = self._get_at_qq(event)
        if not at_qq:
            yield event.plain_result("请@你想删除的好友！")
            return
        
        result = message_processor(
            message="删除牛友",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            at_qq=int(at_qq),
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)

    @filter.command("🔒")
    @filter.command("锁")
    async def cmd_lock_target(self, event: AstrMessageEvent):
        """锁别人"""
        await self.initialize()
        sender_id, sender_name, group_id = self._get_sender_info(event)
        
        at_qq = self._get_at_qq(event)
        if not at_qq:
            yield event.plain_result("请@你想锁的人！")
            return
        
        result = message_processor(
            message="🔒",
            qq=int(sender_id),
            group=int(group_id) if group_id else 0,
            at_qq=int(at_qq),
            nickname=sender_name
        )
        
        if result:
            yield event.plain_result(result)
