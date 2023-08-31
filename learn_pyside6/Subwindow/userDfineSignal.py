
'''
主窗口向子窗口传参
# 1，创建一个信号
# 2，主窗口类中进行定义，在__init__函数外面
# 3，对信号进行绑定：信号名称.connect(具体激活的函数)
# 4，使用 信号名.emit(发送值) 激活信号
'''

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import Signal # 1，创建一个信号

class MyWindow(QWidget):
    sendValueToSubWindow = Signal(str) # 2，类中进行定义，在__init__函数外面

    def __init__(self):
        super().__init__()

        self.lineEditSend = QLineEdit()
        self.btn = QPushButton('发送数据到子窗口')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditSend)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

        self.bind()

    def bind(self): # 3，对信号进行绑定：信号名称.connect(具体激活的函数)
        self.subWindow = SubWindow() # 创建子窗口
        self.sendValueToSubWindow.connect(self.subWindow.lineEditSub.setText)
        self.btn.clicked.connect(self.sendValue)
        self.subWindow.show()

    def sendValue(self): # 4，使用 信号名.emit(发送值) 激活信号
        text = self.lineEditSend.text()
        self.sendValueToSubWindow.emit(text)

class SubWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 接收
        self.lineEditSub = QLineEdit()
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditSub)
        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()