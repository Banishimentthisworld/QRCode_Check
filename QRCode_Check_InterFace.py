# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QRCode_Check_InterFace.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 486)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_Message = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_Message.setObjectName("txt_Message")
        self.gridLayout.addWidget(self.txt_Message, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bn_TopExit = QtWidgets.QPushButton(self.groupBox_2)
        self.bn_TopExit.setObjectName("bn_TopExit")
        self.gridLayout_3.addWidget(self.bn_TopExit, 2, 1, 1, 1)
        self.bn_Min = QtWidgets.QPushButton(self.groupBox_2)
        self.bn_Min.setObjectName("bn_Min")
        self.gridLayout_3.addWidget(self.bn_Min, 0, 1, 1, 1)
        self.bn_Exit = QtWidgets.QPushButton(self.groupBox_2)
        self.bn_Exit.setObjectName("bn_Exit")
        self.gridLayout_3.addWidget(self.bn_Exit, 2, 0, 1, 1)
        self.bn_Start = QtWidgets.QPushButton(self.groupBox_2)
        self.bn_Start.setObjectName("bn_Start")
        self.gridLayout_3.addWidget(self.bn_Start, 0, 0, 1, 1)
        self.bn_Stop = QtWidgets.QPushButton(self.groupBox_2)
        self.bn_Stop.setObjectName("bn_Stop")
        self.gridLayout_3.addWidget(self.bn_Stop, 1, 0, 1, 1)
        self.bn_Top = QtWidgets.QPushButton(self.groupBox_2)
        self.bn_Top.setObjectName("bn_Top")
        self.gridLayout_3.addWidget(self.bn_Top, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self._2 = QtWidgets.QGridLayout(self.groupBox_5)
        self._2.setObjectName("_2")
        self.txt_Num = QtWidgets.QLabel(self.groupBox_5)
        self.txt_Num.setObjectName("txt_Num")
        self._2.addWidget(self.txt_Num, 0, 0, 1, 1)
        self.img_Result = QtWidgets.QLabel(self.groupBox_5)
        self.img_Result.setObjectName("img_Result")
        self._2.addWidget(self.img_Result, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_6.addWidget(self.lineEdit_2, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 1, 2, 1, 1)
        self.cmb_Type = QtWidgets.QComboBox(self.groupBox_4)
        self.cmb_Type.setObjectName("cmb_Type")
        self.gridLayout_6.addWidget(self.cmb_Type, 0, 2, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "扫码枪防呆"))
        self.groupBox_2.setTitle(_translate("MainWindow", "操作"))
        self.bn_TopExit.setText(_translate("MainWindow", " 取消置顶 "))
        self.bn_Min.setText(_translate("MainWindow", "最小化"))
        self.bn_Exit.setText(_translate("MainWindow", "退出"))
        self.bn_Start.setText(_translate("MainWindow", "   开始   "))
        self.bn_Stop.setText(_translate("MainWindow", "暂停"))
        self.bn_Top.setText(_translate("MainWindow", "置顶"))
        self.groupBox_5.setTitle(_translate("MainWindow", "结果输出"))
        self.txt_Num.setText(_translate("MainWindow", "个数"))
        self.img_Result.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/img/OK.png\"/></p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "参数"))
        self.label_2.setText(_translate("MainWindow", "标识："))
        self.label_3.setText(_translate("MainWindow", "数量："))
        self.label.setText(_translate("MainWindow", "机种："))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.action.setText(_translate("MainWindow", "开始"))
        self.action_2.setText(_translate("MainWindow", "暂停"))
        self.action_3.setText(_translate("MainWindow", "退出"))

import QRCode_InterFace_Rcc_rc
