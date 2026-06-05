# 版本更新日志

## v3.0.1 (2026-06-05)

### 🐛 修复

- **修复 get_data_dir 调用** - 移除错误的 `self.get_data_dir()` 调用
- **简化初始化逻辑** - 移除不必要的数据目录获取
- **使用正确的方法** - Star 类没有 `get_data_dir` 方法

---

## v3.0.0 (2026-06-05)

### 🔧 完全重构

- **严格遵循 AstrBot Skills 规范** - 每行代码都符合开发规范
- **插件类规范** - 继承 `Star`，`__init__` 接收 `context: Context` 和 `config: AstrBotConfig`
- **命令注册** - 使用 `@filter.command("name")` 装饰器
- **消息返回** - 使用 `yield event.plain_result("message")`
- **异步规范** - 所有 handler 都是 `async def`
- **配置规范** - `_conf_schema.json` 使用正确的字段类型
- **数据存储** - 使用 `self.get_data_dir()` 获取数据目录

---

## v2.0.4 (2026-06-05)

### 🐛 修复

- 修复消息发送机制
- 使用 `impl_send_message` 参数注入消息发送函数

---

## v2.0.3 (2026-06-05)

### 🔧 修复

- 对照原作者代码逐个文件比对
- 修复配置和数据库路径

---

## v2.0.0 (2026-06-05)

### 🔧 初始重构

- 从 nonebot-plugin-dicky-pk v2.6.5 移植
- 适配 AstrBot 平台
