import time
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class WorkThread(QThread):
    signal = Signal(str) # 1.自定义信号，在__init__()之外

    def __init__(self):
        super().__init__()
        print('run')

    def run(self):
        for i in range(10):
            self.signal.emit(str(i)) # 2.信号的手动触发emit()
            time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lb = QLabel('当前的值为：0')

        # 3.主线程创建子线程示例
        # 加self，不然会被内存回收机制给回收
        self.workThread = WorkThread()

        # 4.主线程对子线程的信号进行绑定
        self.workThread.signal.connect(lambda x: self.lb.setText(f'当前的值为：{x}'))

        self.workThread.started.connect(lambda:print('线程开始'))
        self.workThread.finished.connect(lambda:print('线程结束'))
        self.workThread.finished.connect(lambda:self.workThread.deleteLater())

        # 5.开始子线程
        self.workThread.start()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()