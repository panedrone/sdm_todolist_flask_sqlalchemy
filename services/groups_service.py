from dbal.data_store import scoped_ds
from dbal.group import Group
from dbal.groups_dao_ex import GroupsDaoEx
from dbal.task import Task


def get_all_groups():
    ds = scoped_ds()
    return GroupsDaoEx(ds).get_all_groups()


def get_group(g_id):
    ds = scoped_ds()
    group = GroupsDaoEx(ds).read_group(g_id)
    return group


def create_group(g_name):
    ds = scoped_ds()
    group = Group(g_name=g_name)
    GroupsDaoEx(ds).create_group(group)
    ds.commit()


def update_group(g_id, g_name):
    ds = scoped_ds()
    GroupsDaoEx(ds).rename(g_id, g_name)
    ds.commit()


def delete_group(g_id):
    ds = scoped_ds()
    ds.delete_by_filter(Task, {"g_id": g_id})
    rows_deleted = GroupsDaoEx(ds).delete_group(g_id)
    print(f"rows_deleted: {rows_deleted}")
    ds.commit()
