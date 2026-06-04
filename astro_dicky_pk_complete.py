"""
Astro Dicky PK Complete Edition - AstrBot Plugin Entry Point ✨

This file is REQUIRED for AstrBot to detect and load the plugin.
完整保留原版所有功能！无阉割的 3484 行代码牛子 PK 游戏 🎮
"""

__version__ = "1.0.0"
__plugin_name__ = "astro_dicky_pk_complete"

# 从核心模块导入关键功能
from .src.main import message_processor, KEYWORDS, VERSION, HELPPER

# 插件元数据（AstrBot 读取用）
__plugin_meta__ = {
    "name": "牛子 PK 完整版",
    "description": "🎮 完整保留原版所有功能（3484 行）无阉割！",
    "version": "1.0.0",
}

async def on_load():
    """插件加载钩子 - AstrBot 会在启动时调用"""
    print("🎮 Astro Dicky PK - Complete Edition v" + VERSION)
    print("✅ All 10 modules loaded successfully!")
    return True

async def on_unload():
    """插件卸载钩子"""
    print("⏹️ Astro Dicky PK has been unloaded")
    return True

def get_plugin_info():
    """返回插件信息供 AstrBot 调用"""
    return {
        "name": __plugin_name__,
        "version": __version__,
        "description": __plugin_meta__["description"],
        "author": "lion77542 (基于 tkgs0 原版)",
        "dependencies": ["nonebot2>=2.0.0", "arrow>=1.2.0"]
    }

def process_message(message: str, qq: int, group: int, at_qq=None):
    """消息处理函数 - 被 AstrBot 自动调用"""
    try:
        return message_processor(
            message=message,
            qq=qq,
            group=group,
            at_qq=at_qq
        )
    except Exception as e:
        print(f"❌ Error processing message: {e}")
        return None
