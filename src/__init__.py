"""
Astro Dicky PK Complete Edition - Source Package

Contains all core modules for the full-featured Chinchin PK game.
完整保留原版所有功能！无阉割的牛子 PK 游戏 🎮
"""

from .main import (
    message_processor,
    KEYWORDS,
    VERSION,
    HELPPER,
    Chinchin_intercepor,
)

# 导出主要函数供外部使用
__all__ = [
    'message_processor',
    'KEYWORDS',
    'VERSION',
    'HELPPER',
]
