# coding=utf-8
# @Author : kexhong

def get_codebook_data(fileName="codebook.txt"):
    """
    获取codebook数据
    :param fileName: 文件名
    :return: list
    """
    res = []
    file_data = open(fileName, 'r')
    try:
        lines = file_data.readlines()
        for line in lines:
            res.append(line.split('\t'))

        for line in res:
            line[len(line)-1] = line[len(line)-1].replace('\n', '')
    finally:
        file_data.close()
    print(fileName, "has count = ", len(res) - 1)
    return res
