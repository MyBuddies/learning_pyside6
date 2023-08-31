from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("click",self)
        btn.setGeometry(100,100,200,100) # 位置
        btn.setToolTip("点我有惊喜") # 提示
        btn.setText("reset_text")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()