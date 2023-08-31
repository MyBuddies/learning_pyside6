from PySide6.QtWidgets import(
    QApplication, 
    QMainWindow, 
    QPushButton)

import time

# 伪多线程

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        self.btn = QPushButton('start', self)
        self.btn.clicked.connect(self.long_runing_operation)
        self.show()

    def long_runing_operation(self):
        self.btn.setEnabled(False)
        for i in range(10):
            time.sleep(1)
            QApplication.processEvents()
            print(f'当前进度{i+1}/10')
        self.btn.setEnabled(True)
        


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    # window.show()
    app.exec()