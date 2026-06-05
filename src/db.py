from pathlib import Path
from .utils import ArrowUtil, fixed_two_decimal_digits, NumberUtils
from .config import Config
from .rebirth_view import RebirthSystem_View
from .constants import FarmConst, TimeConst
import sqlite3
import os

sql_ins = None

# AstrBot 数据目录
ASTRBOT_DATA_DIR = Path(os.environ.get('ASTRBOT_DATA_DIR', 'data'))
PLUGIN_DATA_DIR = ASTRBOT_DATA_DIR / 'plugins' / 'astro_dicky_pk_complete'


class Paths:
    @staticmethod
    def base_db_path_v1():
        return PLUGIN_DATA_DIR / 'data'

    @staticmethod
    def base_db_dir():
        return PLUGIN_DATA_DIR / 'data-v2'

    @classmethod
    def sqlite_path(cls):
        return cls.base_db_dir() / 'data.sqlite'


class MigrationHelper:
    @staticmethod
    def old_data_check():
        # check old v1 data exist and tip
        if Paths.base_db_path_v1().exists():
            print(
                "[Chinchin::Deprecated]: 目录 data-v2 新数据已经初始化，旧 v1 版本数据 data 已经不再使用，可以备份后手动删除！"
            )


async def lazy_init_database():
    """异步初始化数据库"""
    global sql_ins
    if sql_ins is not None:
        return
    
    # 确保目录存在
    Paths.base_db_dir().mkdir(parents=True, exist_ok=True)
    
    # 初始化 SQL 连接
    db_path = Paths.sqlite_path()
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    sql_ins = SqlConnection(conn, cursor)
    
    # 创建表
    Sql_UserInfo._sql_create_table_if_not_exists()
    Sql_rebirth._sql_create_table_if_not_exists()
    Sql_badge._sql_create_table_if_not_exists()
    # ... 其他表创建


class SqlConnection:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor


def lazy_init_database_sync():
    """同步初始化数据库（向后兼容）"""
    global sql_ins
    if sql_ins is not None:
        return
    
    # 确保目录存在
    Paths.base_db_dir().mkdir(parents=True, exist_ok=True)
    
    # 初始化 SQL 连接
    db_path = Paths.sqlite_path()
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    sql_ins = SqlConnection(conn, cursor)
    
    # 创建表
    Sql_UserInfo._sql_create_table_if_not_exists()
    Sql_rebirth._sql_create_table_if_not_exists()
    Sql_badge._sql_create_table_if_not_exists()


# 保留原函数作为同步版本
def lazy_init_database():
    """同步初始化数据库"""
    lazy_init_database_sync()


class Sql_UserInfo:
    @staticmethod
    def _empty_data_handler(data: dict):
        if data["latest_speech_nickname"] is None:
            data["latest_speech_nickname"] = ""
        return data

    @staticmethod
    def _sql_create_table():
        return "create table if not exists `info` (`qq` bigint, `latest_speech_nickname` varchar(255), `latest_speech_group` bigint, primary key (`qq`));"

    @classmethod
    def _sql_create_table_if_not_exists(cls):
        if sql_ins:
            sql_ins.cursor.execute(cls._sql_create_table())
            sql_ins.conn.commit()

    @classmethod
    def _sql_insert_single_data(cls, data: dict):
        data = cls._empty_data_handler(data)
        return f'insert into `info` (`latest_speech_group`, `latest_speech_nickname`, `qq`) values (:latest_speech_group, :latest_speech_nickname, {data["qq"]});'

    @staticmethod
    def _sql_select_single_data(qq: int):
        return f"select * from `info` where `qq` = {qq};"

    @staticmethod
    def _sql_check_table_exists():
        return (
            'select count(*) from sqlite_master where type = "table" and name = "info";'
        )

    @classmethod
    def _sql_update_single_data(cls, data: dict):
        data = cls._empty_data_handler(data)
        return f'update `info` set `latest_speech_nickname` = :latest_speech_nickname, `latest_speech_group` = :latest_speech_group where `qq` = {data["qq"]};'

    @staticmethod
    def _sql_batch_select_data(qqs: list):
        return f"select * from `info` where `qq` in {Sql.utils.tupleify(qqs)};"

    @staticmethod
    def _sql_delete_single_data(qq: int):
        return f"delete from `info` where `qq` = {qq};"

    @staticmethod
    def deserialize(data: tuple):
        return {
            "qq": data[0],
            "latest_speech_nickname": data[1],
            "latest_speech_group": data[2],
        }

    @classmethod
    def select_single_data(cls, qq: int):
        sql_ins.cursor.execute(cls._sql_select_single_data(qq))
        one = sql_ins.cursor.fetchone()
        if one is None:
            return None
        return cls.deserialize(one)

    @classmethod
    def select_batch_data_by_qqs(cls, qqs: list):
        sql_ins.cursor.execute(cls._sql_batch_select_data(qqs))
        return [cls.deserialize(data) for data in sql_ins.cursor.fetchall()]

    @classmethod
    def delete_single_data(cls, qq: int):
        sql_ins.cursor.execute(cls._sql_delete_single_data(qq))
        sql_ins.conn.commit()


class Sql_rebirth:
    @staticmethod
    def _sql_create_table():
        return "create table if not exists `rebirth` (`qq` bigint, `latest_rebirth_time` varchar(255), `level` integer, primary key (`qq`));"

    @classmethod
    def _sql_create_table_if_not_exists(cls):
        if sql_ins:
            sql_ins.cursor.execute(cls._sql_create_table())
            sql_ins.conn.commit()

    @staticmethod
    def _sql_insert_single_data(data: dict):
        return f'insert into `rebirth` (`level`, `latest_rebirth_time`, `qq`) values (:level, :latest_rebirth_time, {data["qq"]});'

    @staticmethod
    def _sql_select_single_data(qq: int):
        return f"select * from `rebirth` where `qq` = {qq};"

    @staticmethod
    def _sql_batch_select_data(qqs: list):
        return f"select * from `rebirth` where `qq` in {Sql.utils.tupleify(qqs)};"

    @staticmethod
    def _sql_check_table_exists():
        return 'select count(*) from sqlite_master where type = "table" and name = "rebirth";'

    @staticmethod
    def _sql_update_single_data(data: dict):
        return f'update `rebirth` set `level` = :level, `latest_rebirth_time` = :latest_rebirth_time where `qq` = {data["qq"]};'

    @staticmethod
    def _sql_delete_single_data(qq: int):
        return f"delete from `rebirth` where `qq` = {qq};"

    @staticmethod
    def deserialize(data: tuple):
        return {
            "qq": data[0],
            "latest_rebirth_time": data[1],
            "level": data[2],
        }

    @classmethod
    def select_single_data(cls, qq: int):
        sql_ins.cursor.execute(cls._sql_select_single_data(qq))
        one = sql_ins.cursor.fetchone()
        if one is None:
            return None
        return cls.deserialize(one)

    @classmethod
    def insert_single_data(cls, data: dict):
        sql_ins.cursor.execute(cls._sql_insert_single_data(data), data)
        sql_ins.conn.commit()

    @classmethod
    def update_single_data(cls, data: dict):
        sql_ins.cursor.execute(cls._sql_update_single_data(data), data)
        sql_ins.conn.commit()

    @classmethod
    def delete_single_data(cls, qq: int):
        sql_ins.cursor.execute(cls._sql_delete_single_data(qq))
        sql_ins.conn.commit()

    @classmethod
    def select_batch_data_by_qqs(cls, qqs: list):
        sql_ins.cursor.execute(cls._sql_batch_select_data(qqs))
        return [cls.deserialize(data) for data in sql_ins.cursor.fetchall()]


class DB_Rebirth:
    @staticmethod
    def get_rebirth_data(qq: int):
        return Sql_rebirth.select_single_data(qq)

    @staticmethod
    def insert_rebirth_data(data: dict):
        Sql_rebirth.insert_single_data(data)

    @staticmethod
    def update_rebirth_data(data: dict):
        Sql_rebirth.update_single_data(data)


class Sql_badge:
    @staticmethod
    def _sql_create_table():
        return "create table if not exists `badge` (`qq` bigint, `badge_ids` varchar(255), `glue_me_count` bigint, `glue_target_count` bigint, `glue_plus_count` bigint, `glue_plus_length_total` bigint, `glue_punish_count` bigint, `glue_punish_length_total` bigint, `pk_win_count` bigint, `pk_lose_count` bigint, `pk_plus_length_total` bigint, `pk_punish_length_total` bigint, `lock_me_count` bigint, `lock_target_count` bigint, `lock_plus_count` bigint, `lock_punish_count` bigint, `lock_plus_length_total` bigint, `lock_punish_length_total` bigint, primary key (`qq`));"

    @classmethod
    def _sql_create_table_if_not_exists(cls):
        if sql_ins:
            sql_ins.cursor.execute(cls._sql_create_table())
            sql_ins.conn.commit()

    @staticmethod
    def _sql_insert_single_data(data: dict):
        return f'insert into `badge` (`qq`, `badge_ids`, `glue_me_count`, `glue_target_count`, `glue_plus_count`, `glue_plus_length_total`, `glue_punish_count`, `glue_punish_length_total`, `pk_win_count`, `pk_lose_count`, `pk_plus_length_total`, `pk_punish_length_total`, `lock_me_count`, `lock_target_count`, `lock_plus_count`, `lock_punish_count`, `lock_plus_length_total`, `lock_punish_length_total`) values ({data["qq"]}, :badge_ids, :glue_me_count, :glue_target_count, :glue_plus_count, :glue_plus_length_total, :glue_punish_count, :glue_punish_length_total, :pk_win_count, :pk_lose_count, :pk_plus_length_total, :pk_punish_length_total, :lock_me_count, :lock_target_count, :lock_plus_count, :lock_punish_count, :lock_plus_length_total, :lock_punish_length_total);'

    @staticmethod
    def _sql_select_single_data(qq: int):
        return f"select * from `badge` where `qq` = {qq};"

    @staticmethod
    def _sql_batch_select_data(qqs: list):
        return f"select * from `badge` where `qq` in {Sql.utils.tupleify(qqs)};"

    @staticmethod
    def deserialize(data: tuple):
        return {
            "qq": data[0],
            "badge_ids": data[1] or "",
            "glue_me_count": data[2] or 0,
            "glue_target_count": data[3] or 0,
            "glue_plus_count": data[4] or 0,
            "glue_plus_length_total": data[5] or 0,
            "glue_punish_count": data[6] or 0,
            "glue_punish_length_total": data[7] or 0,
            "pk_win_count": data[8] or 0,
            "pk_lose_count": data[9] or 0,
            "pk_plus_length_total": data[10] or 0,
            "pk_punish_length_total": data[11] or 0,
            "lock_me_count": data[12] or 0,
            "lock_target_count": data[13] or 0,
            "lock_plus_count": data[14] or 0,
            "lock_punish_count": data[15] or 0,
            "lock_plus_length_total": data[16] or 0,
            "lock_punish_length_total": data[17] or 0,
        }

    @classmethod
    def select_single_data(cls, qq: int):
        sql_ins.cursor.execute(cls._sql_select_single_data(qq))
        one = sql_ins.cursor.fetchone()
        if one is None:
            return None
        return cls.deserialize(one)

    @classmethod
    def insert_single_data(cls, data: dict):
        sql_ins.cursor.execute(cls._sql_insert_single_data(data), data)
        sql_ins.conn.commit()

    @classmethod
    def update_badge_ids(cls, qq: int, badge_ids: str):
        sql_ins.cursor.execute(
            f"update `badge` set `badge_ids` = '{badge_ids}' where `qq` = {qq};"
        )
        sql_ins.conn.commit()

    @classmethod
    def select_batch_data_by_qqs(cls, qqs: list):
        sql_ins.cursor.execute(cls._sql_batch_select_data(qqs))
        return [cls.deserialize(data) for data in sql_ins.cursor.fetchall()]


class Sql:
    class utils:
        @staticmethod
        def tupleify(lst: list):
            if len(lst) == 1:
                return f"({lst[0]})"
            return tuple(lst)


class DB_Badge:
    @staticmethod
    def get_badge_data(qq: int):
        return Sql_badge.select_single_data(qq)

    @staticmethod
    def update_badge_ids(qq: int, badge_ids: str):
        Sql_badge.update_badge_ids(qq, badge_ids)

    @staticmethod
    def record_glue_me_count(qq: int):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["glue_me_count"] += 1
            # update
            sql_ins.cursor.execute(
                f"update `badge` set `glue_me_count` = {data['glue_me_count']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_glue_target_count(qq: int):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["glue_target_count"] += 1
            sql_ins.cursor.execute(
                f"update `badge` set `glue_target_count` = {data['glue_target_count']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_glue_plus_count(qq: int):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["glue_plus_count"] += 1
            sql_ins.cursor.execute(
                f"update `badge` set `glue_plus_count` = {data['glue_plus_count']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_glue_plus_length_total(qq: int, length: float):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["glue_plus_length_total"] += length
            sql_ins.cursor.execute(
                f"update `badge` set `glue_plus_length_total` = {data['glue_plus_length_total']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_glue_punish_count(qq: int):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["glue_punish_count"] += 1
            sql_ins.cursor.execute(
                f"update `badge` set `glue_punish_count` = {data['glue_punish_count']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_glue_punish_length_total(qq: int, length: float):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["glue_punish_length_total"] += length
            sql_ins.cursor.execute(
                f"update `badge` set `glue_punish_length_total` = {data['glue_punish_length_total']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_pk_win_count(qq: int):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["pk_win_count"] += 1
            sql_ins.cursor.execute(
                f"update `badge` set `pk_win_count` = {data['pk_win_count']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_pk_lose_count(qq: int):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["pk_lose_count"] += 1
            sql_ins.cursor.execute(
                f"update `badge` set `pk_lose_count` = {data['pk_lose_count']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_pk_plus_length_total(qq: int, length: float):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["pk_plus_length_total"] += length
            sql_ins.cursor.execute(
                f"update `badge` set `pk_plus_length_total` = {data['pk_plus_length_total']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_pk_punish_length_total(qq: int, length: float):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["pk_punish_length_total"] += length
            sql_ins.cursor.execute(
                f"update `badge` set `pk_punish_length_total` = {data['pk_punish_length_total']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_lock_me_count(qq: int):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["lock_me_count"] += 1
            sql_ins.cursor.execute(
                f"update `badge` set `lock_me_count` = {data['lock_me_count']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_lock_target_count(qq: int):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["lock_target_count"] += 1
            sql_ins.cursor.execute(
                f"update `badge` set `lock_target_count` = {data['lock_target_count']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_lock_plus_count(qq: int):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["lock_plus_count"] += 1
            sql_ins.cursor.execute(
                f"update `badge` set `lock_plus_count` = {data['lock_plus_count']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_lock_plus_length_total(qq: int, length: float):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["lock_plus_length_total"] += length
            sql_ins.cursor.execute(
                f"update `badge` set `lock_plus_length_total` = {data['lock_plus_length_total']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_lock_punish_count(qq: int):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["lock_punish_count"] += 1
            sql_ins.cursor.execute(
                f"update `badge` set `lock_punish_count` = {data['lock_punish_count']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def record_lock_punish_length_total(qq: int, length: float):
        data = Sql_badge.select_single_data(qq)
        if data:
            data["lock_punish_length_total"] += length
            sql_ins.cursor.execute(
                f"update `badge` set `lock_punish_length_total` = {data['lock_punish_length_total']} where `qq` = {qq};"
            )
            sql_ins.conn.commit()


# 主数据库操作类
class DB:
    sub_db_info = Sql_UserInfo()
    sub_db_rebirth = DB_Rebirth()
    sub_db_badge = DB_Badge()
    sub_db_farm = None  # 会在下面定义
    sub_db_friends = None  # 会在下面定义

    class utils:
        @staticmethod
        def merge_data(*dicts):
            result = {}
            for d in dicts:
                if d:
                    result.update(d)
            return result

        @staticmethod
        def merge_data_list(dicts_list):
            if not dicts_list:
                return []
            result = []
            for i in range(len(dicts_list[0])):
                merged = {}
                for d in dicts_list:
                    if i < len(d) and d[i]:
                        merged.update(d[i])
                result.append(merged)
            return result

    @staticmethod
    def is_registered(qq: int) -> bool:
        data = Sql_UserInfo.select_single_data(qq)
        return data is not None

    @staticmethod
    def load_data(qq: int) -> dict:
        data = Sql_UserInfo.select_single_data(qq)
        if data is None:
            return {}
        return data

    @staticmethod
    def create_data(data: dict):
        Sql_UserInfo.insert_single_data(data)

    @staticmethod
    def get_data_counts() -> int:
        sql_ins.cursor.execute("select count(*) from `info`;")
        return sql_ins.cursor.fetchone()[0]

    @staticmethod
    def get_top_users(limit: int = 10):
        sql_ins.cursor.execute(
            f"select * from `users` order by `length` desc limit {limit};"
        )
        return sql_ins.cursor.fetchall()

    @staticmethod
    def length_increase(qq: int, length: float):
        sql_ins.cursor.execute(
            f"update `users` set `length` = `length` + {length} where `qq` = {qq};"
        )
        sql_ins.conn.commit()

    @staticmethod
    def length_decrease(qq: int, length: float):
        sql_ins.cursor.execute(
            f"update `users` set `length` = `length` - {length} where `qq` = {qq};"
        )
        sql_ins.conn.commit()

    @staticmethod
    def record_time(qq: int, field: str):
        now = ArrowUtil.get_now_time()
        sql_ins.cursor.execute(
            f"update `users` set `{field}` = '{now}' where `qq` = {qq};"
        )
        sql_ins.conn.commit()

    @staticmethod
    def is_lock_daily_limited(qq: int) -> bool:
        data = Sql_UserInfo.select_single_data(qq)
        if not data:
            return False
        config = Config.get_config("lock_daily_limited")
        return data.get("daily_lock_count", 0) >= config

    @staticmethod
    def is_pk_daily_limited(qq: int) -> bool:
        data = Sql_UserInfo.select_single_data(qq)
        if not data:
            return False
        config = Config.get_config("max_pks_per_day")
        return data.get("daily_pk_count", 0) >= config

    @staticmethod
    def is_glue_daily_limited(qq: int) -> bool:
        data = Sql_UserInfo.select_single_data(qq)
        if not data:
            return False
        config = Config.get_config("glue_daily_limited")
        return data.get("daily_glue_count", 0) >= config

    @staticmethod
    def count_lock_daily(qq: int):
        sql_ins.cursor.execute(
            f"update `users` set `daily_lock_count` = `daily_lock_count` + 1 where `qq` = {qq};"
        )
        sql_ins.conn.commit()

    @staticmethod
    def count_pk_daily(qq: int):
        sql_ins.cursor.execute(
            f"update `users` set `daily_pk_count` = `daily_pk_count` + 1 where `qq` = {qq};"
        )
        sql_ins.conn.commit()

    @staticmethod
    def count_glue_daily(qq: int):
        sql_ins.cursor.execute(
            f"update `users` set `daily_glue_count` = `daily_glue_count` + 1 where `qq` = {qq};"
        )
        sql_ins.conn.commit()

    @staticmethod
    def is_pk_protected(at_qq: int) -> bool:
        data = DB.load_data(at_qq)
        if not data:
            return False
        return data.get("length", 0) < 1  # 保护机制

    @staticmethod
    def make_sure_user_length_not_zero(qq: int):
        data = DB.load_data(qq)
        if data and data.get("length", 0) <= 0:
            sql_ins.cursor.execute(
                f"update `users` set `length` = 0.01 where `qq` = {qq};"
            )
            sql_ins.conn.commit()

    @staticmethod
    def get_batch_users(qqs: list):
        return Sql_UserInfo.select_batch_data_by_qqs(qqs)


# Farm 和 Friends 子数据库会在各自的文件中定义并注册到 DB
