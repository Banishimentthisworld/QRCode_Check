import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pythoncom
import PyHook3 as pyHook
import configparser

from QRCode_Check_InterFace import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 控件初始化
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.bn_Stop.setEnabled(False)
        # 信号槽
        # 退出按钮信号槽
        self.bn_Exit.clicked.connect(self.Exit)
        # 开始按钮信号槽
        self.bn_Start.clicked.connect(self.Start)
        # 下拉菜单改变信号槽
        self.cmb_Type.currentIndexChanged.connect(self.cmbchange)
        # 清除数据信号槽
        self.bn_Zero.clicked.connect(self.clear)
        # 暂停按钮信号槽
        self.bn_Stop.clicked.connect(self.Stop)

        # 全局变量
        global QRcode_Message, img_NG, img_OK, cf, Times, NG_Times
        Times = 0
        NG_Times = 0

        QRcode_Message = ""
        img_NG = QPixmap('NG')
        img_OK = QPixmap('OK')

        # 规格配置
        cf = configparser.ConfigParser()
        cf.read("config.ini")
        sections = cf.sections()
        self.cmb_Type.addItems(sections)
        self.cmb_Type.setCurrentIndex(0)


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
        self.bn_Stop.setEnabled(True)
        self.bn_Start.setEnabled(False)
        def onKeyboardEvent(event):
            global QRcode_Message, img_NG, img_OK, Times, NG_Times
            if str(event.Key) != "Lshift" and str(event.Key).isdigit():
                QRcode_Message = QRcode_Message + str(event.Key)
            elif str(event.Key) == "Return":
                try:
                    if Times < int(self.txt_Num_2.text()):
                        if QRcode_Message[0:4] == self.txt_ID.text():
                            Times += 1
                            self.img_Result.setPixmap(img_OK)
                            self.txt_Message.insertPlainText("\n")
                            self.txt_Message.insertHtml(
                                '<html><head/><body><p><span style=" color:green;font-weight:bold;font-size:45px;">' + str(Times) + ": "+ QRcode_Message + '</span></p></body></html>')
                            self.txt_Message.moveCursor(self.txt_Message.textCursor().End)  # 文本框显示到底部
                            self.txt_Num.setText(str(Times) + "/" + self.txt_Num_2.text())
                        else:
                            Times += 1
                            NG_Times += 1
                            self.img_Result.setPixmap(img_NG)
                            self.txt_Message.insertPlainText("\n")
                            self.txt_Message.insertHtml(
                                '<html><head/><body><p><span style=" color:red;font-weight:bold;font-size:45px;">' + str(Times) + ": " + QRcode_Message + '</span></p></body></html>')
                            self.txt_Message.moveCursor(self.txt_Message.textCursor().End)  # 文本框显示到底部
                            self.txt_Num.setStyleSheet("color:WhiteSmoke;font-size:40px")
                            self.txt_Num.setText(str(Times) + "/" + self.txt_Num_2.text())
                            self.txt_NG.setStyleSheet("color:red;font-size:40px")
                            self.txt_NG.setText("NG:" + str(NG_Times))
                    elif Times == int(self.txt_Num_2.text()):
                        Times += 1
                        self.msg('已检测完整盘，请更换物料并清空计数')

                except:
                    self.msg('请选择类型')

                QRcode_Message = ""



            return True

        # 创建键盘监控句柄
        global hm
        hm = pyHook.HookManager()
        #监控键盘
        hm.KeyDown = onKeyboardEvent
        hm.HookKeyboard()
        #循环获取消息
        pythoncom.PumpMessages()

    def Exit(self):
        os._exit(0)

    def cmbchange(self):

        ID = cf.get(self.cmb_Type.currentText(), "ID")
        Num = cf.get(self.cmb_Type.currentText(), "NUM")
        self.txt_ID.setText(ID)
        self.txt_Num_2.setText(Num)

    def msg(self, message):
        QApplication.setQuitOnLastWindowClosed(False)
        box = QMessageBox(QMessageBox.Information, '警告', message)
        box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | Qt.Tool)
        yes = box.addButton('知道了', QMessageBox.YesRole)
        box.show()
        if box.exec() == 0:
            pass
        else:
            pass

    def error(self, massage):
        error = QMessageBox.warning(None,
                                    'Error',
                                    massage,
                                    QMessageBox.Yes | QMessageBox.No)


    def clear(self):

        global Times, NG_Times
        Times = 0
        NG_Times = 0
        self.txt_Num.setStyleSheet("color:WhiteSmoke;font-size:40px")
        self.txt_Num.setText(str(Times) + "/" + self.txt_Num_2.text())
        self.txt_NG.setStyleSheet("color:red;font-size:40px")
        self.txt_NG.setText("NG:" + str(NG_Times))
        self.txt_Message.insertPlainText("\n")
        self.txt_Message.insertHtml(
            '<html><head/><body><p><span style=" color:#FF6100;font-weight:bold;font-size:45px;">' + "---------------------" + '</span></p></body></html>')
        self.txt_Message.moveCursor(self.txt_Message.textCursor().End)  # 文本框显示到底部

    def Stop(self):
        self.bn_Stop.setEnabled(False)
        self.bn_Start.setEnabled(True)
        global hm
        hm.UnhookKeyboard()

