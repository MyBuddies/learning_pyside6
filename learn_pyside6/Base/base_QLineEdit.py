from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
# from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayOut = QVBoxLayout()

        line = QLineEdit(self)
        line.setPlaceholderText("请输入内容：")

        mainLayOut.addWidget(line)
        self.setLayout(mainLayOut)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()