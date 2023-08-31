from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lb = QLabel('这是主窗口')

        self.subWindow = SubWindow()

        self.btnClose = QPushButton('关闭子窗口')
        self.btnClose.clicked.connect(lambda: self.subWindow.close())

        self.btnShow = QPushButton('显示子窗口')
        self.btnShow.clicked.connect(lambda: self.subWindow.show())

        self.btnHide = QPushButton('隐藏子窗口')
        self.btnHide.clicked.connect(lambda: self.subWindow.hide())

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btnClose)
        self.mainLayout.addWidget(self.btnShow)
        self.mainLayout.addWidget(self.btnHide)
        self.setLayout(self.mainLayout)

class SubWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lb = QLabel('这是个子窗口')
        self.lineEdit = QLineEdit()
        self.lineEdit.setText('这个是子窗口的文本框')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.lineEdit)
        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()