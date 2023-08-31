from PySide6.QtWidgets import QApplication, QWidget
from Ui_login import Ui_Dialog # 第一，导入

class MyWindow(QWidget, Ui_Dialog): # 第二，继承
    def __init__(self):
        super().__init__()

        self.setupUi(self) # 第三，执行

        self.pushButton.clicked.connect(self.loginFunc)

    def loginFunc(self):
        # 拿到账号
        account = self.lineEdit.text()
        # 拿到密码
        password = self.lineEdit_2.text()

        if account == "123" and password == "123":
            print("success login")
        else:
            print("error login")

        

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()