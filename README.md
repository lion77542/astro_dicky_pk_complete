# 🎮 Astro Dicky PK (完整版) - ALL Features Included!

一个基于 AstrBot 平台的**完整功能版**牛子 PK 群聊游戏，源自 [nonebot-plugin-dicky-pk](https://github.com/tkgs0/nonebot-plugin-dicky-pk)。

<div align="center">

**📦 完整保留原版所有功能 · ⚡ 完美适配 AstrBot 平台**

</div>

## ✅ 包含的功能模块

| 功能模块 | 状态 | 文件 | 行数 |
|----------|------|------|------|
| 🎯 **核心 PK 对战** | ✅ 完整 | `main.py` | 980 行 |
| 💾 **数据库系统** | ✅ 完整 | `src/db.py` | 1017 行 |
| 👥 **好友管理系统** | ✅ 完整 | `src/friends.py` | 319 行 |
| 🏆 **徽章成就系统** | ✅ 完整 | `src/badge.py` | 210 行 |
| 🌱 **农场修炼系统** | ✅ 完整 | `src/farm.py` | 180 行 |
| ✨ **转世重生系统** | ✅ 完整 | `src/rebirth.py` | 80 行 |
| ⚙️ **配置管理系统** | ✅ 完整 | `src/config.py` | 176 行 |
| 🔧 **工具函数库** | ✅ 完整 | `src/utils.py` | 189 行 |
| 📝 **常量定义** | ✅ 完整 | `src/constants.py` | 55 行 |
| 🚀 **插件入口** | ✅ 完整 | `__init__.py` | 278 行 |

**总计**: 10 个 Python 文件，**3484 行** 完整代码！

---

## 🎮 完整游戏功能

### 核心对战系统

| 指令 | 说明 |
|------|------|
| `/pk 新 pk` | 发起与他人的 PK 挑战 |
| `启动 pk` | 加入当前 PK 挑战 |
| `拒绝` | 拒绝 PK 邀请 |

### 属性成长系统

| 指令 | 说明 |
|------|------|
| `注册牛子` | 注册自己的牛子 |
| `/牛子排名` / `排行` | 查看全服排行榜 |
| `看牛子` | 查看他人属性 |

### 特殊玩法

| 指令 | 说明 |
|------|------|
| `打胶` | 自我修炼增加属性 |
| `🔒我` / `锁我` | 锁定自己获取属性 |
| `/🔒某人` | 锁住别人获得加成 |

### 农场系统

| 指令 | 说明 |
|------|------|
| `牛子仙境` | 进入农场修炼 |
| `牛子修炼` | 开始修炼，等待奖励 |

### 好友系统

| 指令 | 说明 |
|------|------|
| `牛友` | 查看好友列表 |
| `添加牛友` | 添加好友关系 |
| `删除朋友` | 解除好友关系 |

### 成就系统

| 指令 | 说明 |
|------|------|
| `牛子成就` | 查看已解锁的徽章成就 |

### 转世系统

| 指令 | 说明 |
|------|------|
| `牛子转生` | 尝试转世，提升等级 |

### 其他功能

| 指令 | 说明 |
|------|------|
| `帮助` | 显示所有可用指令 |

---

## 🚀 快速安装

### 方法一：复制完整插件包

```bash
# 插件位置
/app/plugins/astro_dicky_pk_complete/

# 直接复制到 plugins 目录
cp -r astro_dicky_pk_complete /path/to/AstrBot/data/plugins/

# 重启 AstrBot
docker restart astrbot
```

### 方法二：手动部署

```bash
cd /path/to/AstrBot/data/plugins
git clone https://github.com/lion77542/astro_dicky_pk.git astro_dicky_pk_complete
cd astro_dicky_pk_complete

# 安装依赖
pip install -r requirements.txt

# 重启服务
systemctl restart astrbot
```

---

## 📊 项目统计

| 指标 | 数值 |
|------|------|
| **Python 文件数** | 10 个 |
| **总代码行数** | 3,484 行 |
| **代码总大小** | 122.3 KB |
| **数据库表数量** | 7 个核心表 |
| **支持平台** | QQ/Telegram/Discord/Lark |
| **AstrBot 版本** | ≥4.16 |

---

## ⚙️ 配置文件示例

在 AstrBot 配置文件中添加：

```yaml
plugins:
  astro_dicky_pk_complete:
    dicky_pk:
      # PK 配置
      max_pks_per_day: 5        # 每日最大 PK 次数
      pk_cd_time: 300           # PK CD 时间 (秒)
      
      # 属性成长配置
      lock_daily_limited: 10    # 每日锁最多次数
      glue_daily_limited: 5     # 每日打胶最多次数
      
      # 农场配置
      farm_play_time_start: "22:00"   # 农场开放时间
      farm_duration: "2h"              # 修炼持续时间
      farm_min_cost: 10                # 最小修炼消耗 (厘米)
      
      # 好友系统配置
      friends_max: 20            # 最大好友数量
      friend_fee_base: 1         # 基础好友费 (每厘米)
      friend_fee_share: 0.5      # 共享好友附加费
```

---

## 🎁 特色功能详解

### 🌱 农场修炼系统
- 每天特定时间段开放修炼
- 修炼期间无法进行其他操作
- 修炼结束后自动获得大量属性奖励
- 保护机制防止过度修炼

### 🏆 徽章成就系统
- 记录玩家的各类成就
- PK 胜利、失败次数统计
- 解锁特殊称号和徽章
- 成就展示功能

### 👥 好友管理系统
- 添加/删除好友
- 好友共享加成效果
- 每日好友收益结算
- 防止恶意交友机制

### ✨ 转世重生系统
- 通过转世提升等级
- 每次转世有失败惩罚
- 转世后属性加成永久生效
- 多阶段等级晋升

### 🔐 防作弊机制
- 每日次数限制
- CD 冷却时间控制
- 防刷分保护
- 负反馈惩罚机制

---

## 🛠️ 技术架构

```
astro_dicky_pk_complete/
├── __init__.py              # 插件入口 (278 行)
├── src/
│   ├── main.py              # 核心逻辑 (980 行)
│   ├── db.py                # 数据库操作 (1017 行)
│   ├── config.py            # 配置管理 (176 行)
│   ├── utils.py             # 工具函数 (189 行)
│   ├── farm.py              # 农场系统 (180 行)
│   ├── badge.py             # 徽章系统 (210 行)
│   ├── friends.py           # 好友管理 (319 行)
│   ├── rebirth.py           # 转世重生 (80 行)
│   └── constants.py         # 常量定义 (55 行)
├── metadata.yaml            # AstrBot 元数据
├── requirements.txt         # Python 依赖
├── LICENSE                  # MIT 协议
└── README.md               # 使用说明
```

---

## 📋 数据库结构

| 表名 | 说明 | 主要字段 |
|------|------|----------|
| `users` | 用户信息 | qq, length, register_time, ... |
| `rebirths` | 转世记录 | qq, level, latest_rebirth_time |
| `badges` | 徽章成就 | qq, badge_ids, ... 各项计数 |
| `farm` | 农场数据 | qq, status, need_time, ... |
| `friends` | 好友关系 | qq, friends_list, share_count |
| `config` | 配置信息 | key, value |
| `info` | 附加信息 | qq, latest_speech_nickname |

---

## 🔄 更新日志

### v1.0.0 (AstroDicky Complete Edition)
- ✅ 完整移植 nonebot-plugin-dicky-pk 到 AstrBot
- ✅ 保留全部原始功能 (3484 行代码)
- ✅ 优化数据库访问性能
- ✅ 适配多种消息平台
- ✅ 完善的配置选项
- ✅ 详细的文档说明

### 原始版本历史
- v2.6.5 - 最终稳定版
- 包含所有游戏功能和系统

---

## 🤝 贡献与支持

- **原项目作者**: tkgs0
- **原项目地址**: https://github.com/tkgs0/nonebot-plugin-dicky-pk
- **AstrBot 社区**: QQ 群 975206796
- **问题反馈**: GitHub Issues

---

## ⚖️ 开源许可

本项目采用 **MIT License** 开源。

```
Copyright (c) 2024-2026 Astro Dicky PK Community

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

详见 [LICENSE](LICENSE) 文件。

---

<div align="center">

## 🌟 Star 这个仓库支持我们！

感谢你的关注和使用！✨

*祝你在牛子宇宙中玩得开心！* 🎮

</div>
