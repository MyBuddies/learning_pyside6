import time
from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

# 实例化创建多线程

class WorkThread(QObject):
    signal = Signal(str) # 1.自定义信号，在__init__()之外

    def __init__(self):
        super().__init__()
        print('run')

    def run(self):
        for i in range(10):
            self.signal.emit(str(i)) # 2.信号的手动触发emit()
            # print(i)
            time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lb = QLabel('当前的值为：0')

        self.workThread = WorkThread()
        self.threadList = QThread()
        self.workThread.moveToThread(self.threadList)
        self.workThread.signal.connect(lambda x: self.lb.setText(f'当前的值为：{x}'))
        self.threadList.started.connect(self.workThread.run)
        self.threadList.finished.connect(lambda:print('finished'))

        self.threadList.start()

        

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()