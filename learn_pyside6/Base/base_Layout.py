from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QPushButton, QLabel, QLineEdit
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 登陆页面

        # # 方式 1       
        # self.mainLayout = QVBoxLayout() # 垂直控件

        # self.userLayout = QHBoxLayout() # 水平控件
        # self.userLayout.addWidget(QLabel("用户名"))
        # self.userLayout.addWidget(QLineEdit())
        # self.mainLayout.addLayout(self.userLayout)

        # self.passwordLayout = QHBoxLayout()
        # self.passwordLayout.addWidget(QLabel("密码"))
        # self.passwordLayout.addWidget(QLineEdit())
        # self.mainLayout.addLayout(self.passwordLayout)

        # self.mainLayout.addWidget(QPushButton("登陆"))

        # self.setLayout(self.mainLayout)

        # # 方式 2
        # self.mainLayout = QVBoxLayout()
        
        # self.formLayout = QFormLayout() # 表单控件
        # self.formLayout.addRow("用户名", QLineEdit())
        # self.formLayout.addRow("密码", QLineEdit())
        # self.formLayout.addWidget(QPushButton("登陆"))

        # self.mainLayout.addLayout(self.formLayout)

        # self.setLayout(self.mainLayout)

        # 方式 3
        self.mainLayout = QVBoxLayout()

        self.gridLayout = QGridLayout() # 网格控件
        self.gridLayout.addWidget(QLabel("用户名"), 0, 0)
        self.gridLayout.addWidget(QLineEdit(), 0, 1)

        self.gridLayout.addWidget(QLabel("密码"), 1, 0)
        self.gridLayout.addWidget(QLineEdit(), 1, 1)

        self.gridLayout.addWidget(QPushButton("登陆"), 2, 0, 1, 2)

        self.mainLayout.addLayout(self.gridLayout)
        self.setLayout(self.mainLayout)

    
    
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()