
'''
子窗口向主窗口传参
# 1，创建一个信号
# 2，类中进行定义，在__init__函数外面
# 3，对信号进行绑定：信号名称.connect(具体激活的函数)
# 4，使用 信号名.emit(发送值) 激活信号
'''

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import Signal # 1，创建一个信号

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口')
        self.resize(300, 200)

        self.lineEditShow = QLineEdit()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditShow)
        self.setLayout(self.mainLayout)

        self.bind()

    def bind(self):
        self.subWindow = SubWindow(self) # 创建子窗口
        self.subWindow.show() # 显示子窗口


class SubWindow(QWidget):
    sendValueToMain = Signal(str)
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('子窗口')
        self.resize(300, 200)
        self.parent = parent
        self.move(5, 5)
      
        self.lineEditSub = QLineEdit()
        self.btn = QPushButton('发送数据到主窗口')
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditSub)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

        self.bind()

    def bind(self):
        self.sendValueToMain.connect(self.parent.lineEditShow.setText)
        self.btn.clicked.connect(self.sendValue)

    def sendValue(self):
        self.sendValueToMain.emit(self.lineEditSub.text())

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()