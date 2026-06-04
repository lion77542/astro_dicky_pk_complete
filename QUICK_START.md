# 🚀 Astro Dicky PK - 快速开始指南

## ✅ 系统要求

- **AstrBot**: ≥ 4.16
- **Python**: 3.9+
- **数据库**: SQLite / MySQL（可选）

---

## 📦 一键安装（推荐）

### 方法一：通过 AstrBot 插件市场

在 AstrBot 控制面板中访问插件商店，搜索 `astro_dicky_pk_complete` 即可安装！

### 方法二：Git 克隆（推荐用于开发者）

```bash
cd /path/to/AstrBot/data/plugins
git clone https://github.com/lion77542/astro_dicky_pk_complete.git
cd astro_dicky_pk_complete
pip install -r requirements.txt
```

### 方法三：下载压缩包

访问 https://github.com/lion77542/astro_dicky_pk_complete/archive/main.zip

解压后放入 `plugins` 目录即可。

---

## ⚙️ 配置步骤

编辑 AstrBot 配置文件 `config.yaml`:

```yaml
plugins:
  astro_dicky_pk_complete:
    dicky_pk:
      # ========== PK 配置 ==========
      max_pks_per_day: 5            # 每日最大 PK 次数
      pk_cd_time: 300               # PK CD 冷却时间 (秒)
      
      # ========== 农场系统 ==========
      farm_play_time_start: "22:00"     # 农场开放时间 (HH:MM)
      farm_duration: "2h"                 # 修炼持续时间
      
      # ========== 好友系统 ==========
      friends_max: 20                     # 最大好友数量
      friend_fee_base: 1                  # 基础好友费
      
      # ========== 转世系统 ==========
      rebirth_exp_required: 100           # 转世所需经验
      rebirth_success_rate: 0.7           # 成功率
```

重启 AstrBot 使配置生效！

---

## 🎮 游戏指令

### 🔥 核心对战
```
/pk 新 pk          # 发起 PK 挑战
启动 pk           # 加入当前 PK  
拒绝              # 拒绝 PK 邀请
```

### 📊 属性成长
```
注册牛子          # 注册自己的牛子
牛子排名 / 排行   # 查看全服排行榜
看牛子 @某人      # 查看他人属性
打胶              # 自我修炼增加属性
🔒我 / 锁我       # 锁定自己获得属性
```

### 🌱 农场系统
```
牛子仙境          # 查看农场状态
牛子修炼          # 开始修炼（等待奖励）
```

### 👥 好友管理
```
牛友              # 查看好友列表和收益
添加牛友 @某人    # 添加好友关系
删除朋友 @某人    # 解除好友关系
```

### 🏆 成就系统
```
牛子成就          # 查看已解锁的徽章
```

### ✨ 转世重生
```
牛子转生          # 尝试转世提升等级
```

### ❓ 其他
```
帮助              # 显示所有指令
```

---

## 📋 功能清单

| 模块 | 说明 | 文件 |
|------|------|------|
| 🎯 PK 对战 | 属性比拼、随机事件 | `src/main.py` |
| 💾 数据库 | 用户数据持久化 | `src/db.py` |
| 🌱 农场 | 定时开放修炼 | `src/farm.py` |
| 🏆 徽章 | 成就解锁 | `src/badge.py` |
| 👥 好友 | 社交系统 | `src/friends.py` |
| ✨ 转世 | 等级晋升 | `src/rebirth.py` |
| ⚙️ 配置 | 灵活设置 | `src/config.py` |

**总计**: 10 个 Python 文件，3,484 行完整代码！

---

## 💡 常见问题

### Q: 插件不生效怎么办？
A: 
1. 检查 AstrBot 版本是否≥4.16
2. 确认 `metadata.yaml` 格式正确
3. 查看日志确认插件加载状态
4. 重启 AstrBot

### Q: 如何修改配置参数？
A: 编辑 `config.yaml` 中的 `dicky_pk` 部分，重启服务。

### Q: 数据库在哪里？
A: SQLite 默认位于 AstrBot 的 `data` 目录下，MySQL 需自行配置。

---

## 🔗 相关链接

- 📚 项目主页：https://github.com/lion77542/astro_dicky_pk_complete
- 🐛 问题反馈：GitHub Issues
- 📖 原版作者：tkgs0 ([nonebot-plugin-dicky-pk](https://github.com/tkgs0/nonebot-plugin-dicky-pk))
- 💬 官方 QQ 群：975206796

---

<div align="center">

## 🌟 如果觉得有用，请 Star 支持!

感谢你的使用和分享! 🎮✨

*祝你在牛子宇宙中玩得开心!*

**版本**: v1.0.0 Complete Edition  
**发布日期**: 2026-06-04

</div>
