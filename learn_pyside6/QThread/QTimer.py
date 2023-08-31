from PySide6.QtWidgets import(
    QApplication, 
    QWidget, 
    QVBoxLayout, 
    QPushButton, 
    QLabel)

from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer

import os
from pathlib import Path
os.chdir(Path(__file__).parent.absolute())
print(os.getcwd())

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        self.count = 0
        self.picList = ['./pic/1.png', './pic/2.png', './pic/3.png']

        self.timer = QTimer()
        self.timer.timeout.connect(self.timerOut) # timeout在指定时间内无限循环

        self.lb = QLabel()
        self.lb.setPixmap(QPixmap('./pic/1.png'))
        self.btn = QPushButton("开始计时")
        self.btn.clicked.connect(lambda:self.timer.start(500))# 调用开始才可以使用timer

        self.mainLayot = QVBoxLayout()
        self.mainLayot.addWidget(self.lb)
        self.mainLayot.addWidget(self.btn)
        self.setLayout(self.mainLayot)

    def timerOut(self):
        self.count += 1
        self.index = self.count % len(self.picList)
        self.lb.setPixmap(QPixmap(self.picList[self.index]))


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()