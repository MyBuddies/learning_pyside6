from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

# 信号与槽
# Signal and Slot

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayOut = QVBoxLayout()
        
        button = QPushButton("按钮")
        button.clicked.connect(self.hello) # 每点一次“按钮”就显示hello world
       

        mainLayOut.addWidget(button)
        self.setLayout(mainLayOut)
    
    def hello(self):
        print("hello world!")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()