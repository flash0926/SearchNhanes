# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import FileUtil
import Utils
import QTList
from MainUI import MainUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi

"""
工程包含内容
1.登录
2.更新 codebook
3.打开每个nhanes的网站
4.一些咨询
"""


def login():
    return True


def update_codebook():
    pass


def app_start():
    if login():
        update_codebook()
    data = FileUtil.get_codebook_data()
    search_res = Utils.search_data(data, "mcq366d")
    print(search_res)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)
    # 创建窗口
    mainWindow = MainUI()
    mainWindow.show()
    #程序正式启动
    app_start()
    sys.exit(app.exec())
