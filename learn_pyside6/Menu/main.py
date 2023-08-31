from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from Ui_menu import Ui_MainWindow

'''
-创建一个菜单栏
--1，窗体必须是QmainWindow
--2，使用qtDesigner对菜单栏进行添加
--3，编写程序，通过调用Action的triggered方法来触发函数
'''


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 触发菜单栏的信号
        self.actionOpen.triggered.connect(lambda:print('打开'))
        self.actionExit.triggered.connect(lambda:print('退出'))
        self.actionAdd.triggered.connect(lambda:print('添加'))

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()