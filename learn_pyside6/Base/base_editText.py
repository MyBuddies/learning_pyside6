from PySide6.QtWidgets import QApplication, QWidget, QPlainTextEdit, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        textEdit = QPlainTextEdit()
        textEdit.setPlainText("这是一个标题")
        textEdit.appendPlainText("这是一个段落")

        btn = QPushButton("追加文本")
        btn.clicked.connect(lambda: textEdit.appendPlainText("追加段落"))

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(textEdit)
        mainLayout.addWidget(btn)
        self.setLayout(mainLayout)
    
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()