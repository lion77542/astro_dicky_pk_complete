"""
Astro Dicky PK - Complete Edition
牛子 PK 完整版 - AstrBot 标准化插件入口

✨ Full port with ALL original features preserved!
✅ Compatible with AstrBot >= 4.16
🎮 Supports: QQ/Telegram/Discord/Lark
"""

from .src.main import message_processor, KEYWORDS, VERSION, HELPPER

__version__ = "1.0.0"
__plugin_name__ = "astro_dicky_pk_complete"

# 插件元数据（AstrBot 会自动读取）
__plugin_meta__ = {
    "name": "牛子 PK 完整版",
    "description": "🎮 完整保留原版所有功能",
    "version": "1.0.0",
    "author": "lion77542 (移植自 tkgs0)",
}

# 启动回调
async def on_load():
    """插件加载时执行"""
    print("🎮 Astro Dicky PK - Complete Edition v" + VERSION)
    return True

# 停止回调  
async def on_unload():
    """插件停止时执行"""
    print("⏹️ Astro Dicky PK 已停止")
    return True

# 消息处理入口
async def handle_message(bot, event, context):
    """处理群聊消息"""
    # 获取消息内容
    if hasattr(event, 'get_content'):
        msg_content = event.get_content()
    else:
        return False
    
    # 获取发送者信息
    sender_id = getattr(event, 'get_sender_id', lambda: 'unknown')()
    sender_name = getattr(event, 'get_sender_name', lambda: 'unknown')()
    
    # 调用原始核心逻辑
    try:
        from .src.main import LazyDBInitializer
        
        # 初始化数据库
        lazy_db = LazyDBInitializer()
        await lazy_db.init()
        
        # 处理消息
        result = message_processor(
            message=msg_content,
            qq=int(sender_id),
            group=getattr(event, 'group_id', 0),
            nickname=sender_name
        )
        return result
    except Exception as e:
        print(f"❌ 处理消息失败：{e}")
        return False

# 暴露给外部使用
def process_chinchin_message(message: str, qq: int, group: int, at_qq=None):
    """快速消息处理函数"""
    return message_processor(
        message=message,
        qq=qq,
        group=group,
        at_qq=at_qq
    )
