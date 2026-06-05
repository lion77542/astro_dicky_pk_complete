# 🎮 Astro Dicky PK (完整版) - v2.0.0

一个基于 AstrBot 平台的**完整功能版**牛子 PK 群聊游戏，源自 [nonebot-plugin-dicky-pk](https://github.com/tkgs0/nonebot-plugin-dicky-pk)。

<div align="center">

**📦 完整保留原版所有功能 · ⚡ 完美适配 AstrBot 插件规范**

</div>

## ✅ 功能完整性检查

| 功能模块 | 状态 | 说明 |
|----------|------|------|
| 🎯 **核心 PK 对战** | ✅ 完整 | PK 挑战、属性比拼、胜负判定 |
| 💾 **数据库系统** | ✅ 完整 | 7张核心表，SQLite 存储 |
| 👥 **好友管理系统** | ✅ 完整 | 添加/删除好友、共享加成 |
| 🏆 **徽章成就系统** | ✅ 完整 | 记录战绩、解锁称号 |
| 🌱 **农场修炼系统** | ✅ 完整 | 定时开放、修炼奖励 |
| ✨ **转世重生系统** | ✅ 完整 | 等级晋升、永久增益 |
| ⚙️ **配置管理系统** | ✅ 完整 | AstrBot 配置界面支持 |
| 🔧 **工具函数库** | ✅ 完整 | 通用工具函数 |

---

## 🎮 游戏指令

### 基础指令

| 指令 | 说明 |
|------|------|
| `牛子帮助` / `帮助` | 显示所有可用指令 |
| `注册牛子` | 注册自己的牛子 |
| `牛子` | 查看自己的牛子信息 |
| `牛子排名` / `排行` | 查看全服排行榜 |

### 对战指令

| 指令 | 说明 |
|------|------|
| `@某人 pk` | 发起 PK 挑战 |
| `🔒我` / `锁我` | 锁定自己获取属性 |
| `@某人 🔒` | 锁住别人获得加成 |
| `打胶` | 自我修炼增加属性 |
| `@某人 打胶` | 帮别人打胶 |

### 农场系统

| 指令 | 说明 |
|------|------|
| `牛子仙境` | 查看农场状态 |
| `牛子修炼` | 开始修炼 |

### 好友系统

| 指令 | 说明 |
|------|------|
| `牛友` | 查看好友列表 |
| `@某人 添加牛友` | 添加好友 |
| `@某人 删除牛友` | 删除好友 |

### 其他系统

| 指令 | 说明 |
|------|------|
| `牛子成就` | 查看已解锁的徽章成就 |
| `牛子转生` | 尝试转世提升等级 |

---

## 🚀 安装方法

### 方法一：AstrBot 插件市场（推荐）

在 AstrBot 管理界面搜索 `astro_dicky_pk_complete` 并安装。

### 方法二：手动安装

```bash
cd /path/to/AstrBot/data/plugins
git clone https://github.com/lion77542/astro_dicky_pk_complete.git
cd astro_dicky_pk_complete
# 重启 AstrBot
```

### 方法三：直接复制

```bash
# 将整个插件目录复制到 AstrBot 插件目录
cp -r astro_dicky_pk_complete /path/to/AstrBot/data/plugins/
# 重启 AstrBot
```

---

## ⚙️ 配置说明

插件支持通过 AstrBot 管理界面进行配置，也可以手动编辑配置文件。

### 配置参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `max_pks_per_day` | int | 5 | 每日最大 PK 次数 |
| `pk_cd_time` | int | 300 | PK 冷却时间（秒） |
| `lock_daily_limited` | int | 10 | 每日锁最多次数 |
| `glue_daily_limited` | int | 5 | 每日打胶最多次数 |
| `new_chinchin_length_random_min` | float | 5.0 | 新注册最小长度 |
| `new_chinchin_length_random_max` | float | 15.0 | 新注册最大长度 |

---

## 📊 技术规格

| 指标 | 数值 |
|------|------|
| **AstrBot 版本** | ≥ 4.16, < 5 |
| **Python 版本** | 3.9+ |
| **数据库** | SQLite |
| **支持平台** | QQ / Telegram / Discord / Lark |
| **插件版本** | v2.0.0 |

---

## 📁 项目结构

```
astro_dicky_pk_complete/
├── __init__.py              # 插件入口 (AstrBot 标准)
├── src/
│   ├── main.py              # 核心逻辑
│   ├── db.py                # 数据库操作
│   ├── config.py            # 配置管理
│   ├── utils.py             # 工具函数
│   ├── farm.py              # 农场系统
│   ├── badge.py             # 徽章系统
│   ├── friends.py           # 好友管理
│   ├── rebirth.py           # 转世重生
│   └── constants.py         # 常量定义
├── metadata.yaml            # 插件元数据
├── _conf_schema.json        # 配置 schema
├── requirements.txt         # 依赖说明
├── CHANGELOG.md             # 更新日志
├── LICENSE                  # MIT 协议
└── README.md                # 本文件
```

---

## 🔄 版本更新

### v2.0.0 (2026-06-05)
- ✅ 完全重构为 AstrBot 标准插件
- ✅ 使用 `@register` 和 `@filter.command()` 装饰器
- ✅ 修复数据库路径，使用 AstrBot 数据目录
- ✅ 添加配置文件支持
- ✅ 移除不必要依赖

### v1.0.0
- ✅ 从 nonebot-plugin-dicky-pk v2.6.5 完整移植
- ✅ 保留所有原始功能

---

## 🤝 贡献与支持

- **原项目作者**: tkgs0
- **原项目地址**: https://github.com/tkgs0/nonebot-plugin-dicky-pk
- **AstrBot 社区**: QQ 群 975206796
- **问题反馈**: [GitHub Issues](https://github.com/lion77542/astro_dicky_pk_complete/issues)

---

## ⚖️ 开源许可

本项目采用 **MIT License** 开源。

---

<div align="center">

## 🌟 Star 这个仓库支持我们！

感谢你的关注和使用！✨

*祝你在牛子宇宙中玩得开心！* 🎮

</div>
