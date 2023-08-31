from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFontDialog, QTextEdit, QPushButton, QColorDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.edit = QTextEdit()
        self.btn = QPushButton('点我选择字体')
        self.btn.clicked.connect(self.changeFont)
        self.btn2 = QPushButton('点我选择字体颜色')
        self.btn2.clicked.connect(self.changeColor)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.edit)
        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.btn2)
        self.setLayout(self.mainLayout)

    def changeFont(self):
        ok, font = QFontDialog.getFont()
        if not ok:return
        self.edit.setFont(font)
    
    def changeColor(self):
        color = QColorDialog.getColor()
        self.edit.setTextColor(color)

if __name__ == '__main__':
    app =QApplication([])
    window = MyWindow()
    window.show()
    app.exec()