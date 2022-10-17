# coding=utf-8

# @Author : kexhong
# 程序主窗口应用

import sys
# QtCore是Qt的精髓（包括五大模块：元对象系统，属性系统，对象模型，对象树，信号槽）
from PyQt5.QtCore import *
# QtGui 显示应用程序图标，工具提示和各种鼠标光标。
from PyQt5.QtGui import *
# Qt Widgets模块提供了一组UI元素来创建经典的桌面风格的用户界面。
from PyQt5.QtWidgets import *


class MainUI(QWidget):
    def __init__(self):
        super(MainUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('NHanes工具')
        self.resize(400, 400)
        layout = QVBoxLayout()
        self.btn = QPushButton("关闭")
        self.btn.clicked.connect(self.close)
        layout.addWidget(self.btn)
        self.setLayout(layout)
