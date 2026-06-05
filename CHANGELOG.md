# 版本更新日志

## v2.0.3 (2026-06-05)

### 🔧 规范化修复

- **完全恢复原作者代码** - 对照 tkgs0/nonebot-plugin-dicky-pk 逐个文件比对
- **修复配置路径** - `src/config.py` 使用 AstrBot 数据目录
- **修复数据库路径** - `src/db.py` 使用 AstrBot 数据目录
- **确保功能完整** - 所有 src/ 文件与原作者完全一致

---

## v2.0.1 (2026-06-05)

### 🐛 修复

- 修复插件入口文件，使用正确的 `main.py` 作为入口
- 删除旧的 `__init__.py` 和 `astro_dicky_pk_complete.py` 文件
- 使用 `Star` 基类和 `@register` 装饰器符合 AstrBot 规范

---

## v2.0.0 (2026-06-05)

### 🔧 规范化重构

- **完全重构插件入口** - 符合 AstrBot 标准插件规范
  - 使用 `@register` 装饰器注册插件
  - 继承 `Star` 基类
  - 使用 `@filter.command()` 装饰器处理命令
  - 支持异步初始化和消息处理

- **修复依赖问题**
  - 移除 `nonebot2` 依赖
  - 精简 `requirements.txt`

- **修复数据库路径**
  - 使用 AstrBot 数据目录 (`data/plugins/astro_dicky_pk_complete/`)
  - 自动创建必要目录

- **添加配置文件支持**
  - 创建 `_conf_schema.json` 支持 AstrBot 配置管理
  - 支持在 AstrBot 管理界面配置插件参数

- **更新元数据**
  - 版本号：v1.0.0 → v2.0.0
  - 完善 `metadata.yaml` 描述信息
  - 添加更新日志

### ✅ 功能完整性

所有原版功能已完整保留：
- ✅ 核心 PK 对战系统
- ✅ 属性成长系统（注册、打胶、锁）
- ✅ 农场修炼系统
- ✅ 好友管理系统
- ✅ 徽章成就系统
- ✅ 转世重生系统
- ✅ 数据库系统（7张表）

---

## v1.0.0 (初始版本)

- 从 nonebot-plugin-dicky-pk v2.6.5 完整移植
- 保留所有原始功能（3484 行代码）
- 适配 AstrBot 平台
