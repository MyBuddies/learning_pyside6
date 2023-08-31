from PySide6.QtWidgets import QApplication, QWidget
from Ui_calculate import Ui_Form # 第一，导入

class MyWindow(QWidget, Ui_Form): # 第二，继承
    def __init__(self):
        super().__init__()

        self.setupUi(self) # 第三，执行

        self.result = ""

        self.bind()

    def bind(self):
        self.pushButton_0.clicked.connect(lambda:self.addNumber("0"))
        self.pushButton_1.clicked.connect(lambda:self.addNumber("1"))
        self.pushButton_2.clicked.connect(lambda:self.addNumber("2"))
        self.pushButton_3.clicked.connect(lambda:self.addNumber("3"))
        self.pushButton_4.clicked.connect(lambda:self.addNumber("4"))
        self.pushButton_5.clicked.connect(lambda:self.addNumber("5"))
        self.pushButton_6.clicked.connect(lambda:self.addNumber("6"))
        self.pushButton_7.clicked.connect(lambda:self.addNumber("7"))
        self.pushButton_8.clicked.connect(lambda:self.addNumber("8"))
        self.pushButton_9.clicked.connect(lambda:self.addNumber("9"))
        self.pushButton_plus.clicked.connect(lambda:self.addNumber("+"))
        self.pushButton_sub.clicked.connect(lambda:self.addNumber("-"))
        self.pushButton_mul.clicked.connect(lambda:self.addNumber("*"))
        self.pushButton_div.clicked.connect(lambda:self.addNumber("/"))
        self.pushButton_dot.clicked.connect(lambda:self.addNumber("."))
        self.pushButton_enter.clicked.connect(self.equal)
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_clear.clicked.connect(self.clear)
    
    def addNumber(self, number):
        self.lineEdit.clear()
        self.result += number
        self.lineEdit.setText(str(self.result))

    def equal(self):
        self.numberResult = eval(self.result)
        self.lineEdit.setText(str(self.numberResult))

    def back(self):
        self.result = self.result[:-1]
        self.lineEdit.setText(str(self.result))

    def clear(self):
        self.result = ""
        self.lineEdit.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()