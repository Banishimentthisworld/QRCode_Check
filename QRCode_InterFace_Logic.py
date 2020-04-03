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
        self.bn_Exit.clicked.connect(self.close)
        self.bn_Start.clicked.connect(self.Start)

        # 全局变量
        global QRcode_Message
        QRcode_Message = ""


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
            global QRcode_Message
            if str(event.Key) != "Return":
                QRcode_Message = QRcode_Message + str(event.Key)
            else:
                print(QRcode_Message)
                QRcode_Message = ""
            return True

        # 创建键盘监控句柄
        hm = pyHook.HookManager()
        #监控键盘
        hm.KeyDown = onKeyboardEvent
        hm.HookKeyboard()
        #循环获取消息
        pythoncom.PumpMessages()


