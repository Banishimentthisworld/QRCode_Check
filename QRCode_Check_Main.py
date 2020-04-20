from PyQt5 import QtWidgets
import sys
from QRCode_InterFace_Logic import MainWindow
import qdarkstyle
# import win32gui, win32ui, win32con, win32api
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    # 暗黑风格渲染
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    # h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    # print(mainWindow.size())
    # mainWindow.move(0,h-359)
    mainWindow.show()
    sys.exit(app.exec_())
