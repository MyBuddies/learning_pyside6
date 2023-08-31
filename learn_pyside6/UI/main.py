from PySide6.QtWidgets import QApplication, QWidget
from Ui_calculate import Ui_Form # 第一，导入

class MyWindow(QWidget, Ui_Form): # 第二，继承
    def __init__(self):
        super().__init__()

        self.setupUi(self) # 第三，执行

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()