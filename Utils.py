# coding=utf-8
# @Author : kexhong


def _has_str(data, strs, search_field):
    """
    检查是否包含检索的字符串
    :param data:
    :param strs:
    :param searchIndex:
    :return:
    """
    for s in strs:
        for i in search_field:
            if s in data[i]:
                return True
    return False


def search_data(data, search_str, search_field=None):
    """
    搜索数据 返回一个列表
    :param search_str:
    :param data:
    :param search_field: 包含head的所有下标
    :return:
    """
    if search_str == "":
        return []
    search_split = search_str.split(',')
    res = []
    if search_field is None:
        search_field = []
        for i in range(len(data[0])):
            search_field.append(i)

    for line in data:
        if _has_str(line, search_split, search_field):
            res.append(line)

    return res
