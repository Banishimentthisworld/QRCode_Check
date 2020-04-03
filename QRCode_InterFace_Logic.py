import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pythoncom
import PyHook3 as pyHook

from QRCode_Check_InterFace import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 控件初始化
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 信号槽
        # 退出按钮信号槽
        self.bn_Exit.clicked.connect(self.Exit)
        self.bn_Start.clicked.connect(self.Start)

        # 全局变量
        global QRcode_Message, img_NG, img_OK
        QRcode_Message = ""
        img_NG = QPixmap('NG')
        img_OK = QPixmap('OK')



    # 重写鼠标移动事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


    def Start(self):
        def onKeyboardEvent(event):
            global QRcode_Message, img_NG, img_OK
            if str(event.Key) != "Lshift" and str(event.Key).isdigit():
                QRcode_Message = QRcode_Message + str(event.Key)
            elif str(event.Key) == "Return":
                if QRcode_Message[0:4] == "2209":
                    self.img_Result.setPixmap(img_OK)
                else:
                    self.img_Result.setPixmap(img_NG)
                self.txt_Message.insertPlainText("\n")
                self.txt_Message.insertHtml(
                    '<html><head/><body><p><span style=" color:green;font-weight:bold;font-size:45px;">' + QRcode_Message + '</span></p></body></html>')
                self.txt_Message.moveCursor(self.txt_Message.textCursor().End)  # 文本框显示到底部
                print(QRcode_Message[0:4])

                QRcode_Message = ""


            return True

        # 创建键盘监控句柄
        hm = pyHook.HookManager()
        #监控键盘
        hm.KeyDown = onKeyboardEvent
        hm.HookKeyboard()
        #循环获取消息
        pythoncom.PumpMessages()

    def Exit(self):
        os._exit(0)


