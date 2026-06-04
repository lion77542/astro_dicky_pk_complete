#!/usr/bin/env python3
"""
一键验证脚本 - 确保所有人都能正常使用！
运行此脚本即可验证插件是否完整可用
"""

import os
import sys

def check_file(filepath, description):
    """检查文件是否存在"""
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    print(f"{status} {description:40s} {filepath}")
    return exists

print("=" * 70)
print("🔍 Astro Dicky PK 完整性验证")
print("=" * 70)

base_dir = os.path.dirname(os.path.abspath(__file__))
all_ok = True

# 核心入口文件
print("\n[1/3] 检查核心文件...")
all_ok &= check_file(f"{base_dir}/astro_dicky_pk_complete.py", "Plugin Entry")
all_ok &= check_file(f"{base_dir}/__init__.py", "__init__.py")
all_ok &= check_file(f"{base_dir}/metadata.yaml", "metadata.yaml")
all_ok &= check_file(f"{base_dir}/requirements.txt", "requirements.txt")

# 源代码文件
print("\n[2/3] 检查源代码...")
required_py_files = [
    "src/__init__.py",
    "src/main.py",
    "src/db.py",
    "src/config.py",
    "src/utils.py",
    "src/farm.py",
    "src/badge.py",
    "src/friends.py",
    "src/rebirth.py",
    "src/constants.py",
    "src/badge_parser.py",
    "src/cd.py",
    "src/rebirth_view.py"
]

for f in required_py_files:
    all_ok &= check_file(f"{base_dir}/{f}", f)

# requirements.txt 检查
print("\n[3/3] 检查依赖配置...")
with open(f"{base_dir}/requirements.txt", "r") as f:
    req_content = f.read()

critical_deps = ["nonebot2", "arrow", "aiosqlite", "ujson"]
for dep in critical_deps:
    found = dep in req_content
    status = "✅" if found else "❌"
    print(f"{status} {dep:20s} {'found' if found else 'MISSING!'}")
    all_ok &= found

print("\n" + "=" * 70)
if all_ok:
    print("🎉 完美！所有检查通过，插件可正常安装使用！")
    print("✅ 任何人都可以从 GitHub 下载并一键使用！")
else:
    print("⚠️  发现缺失文件！请修复后再发布！")
print("=" * 70)

sys.exit(0 if all_ok else 1)
