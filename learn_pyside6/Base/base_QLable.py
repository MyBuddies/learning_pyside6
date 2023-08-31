from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayOut = QVBoxLayout()
        
        lb = QLabel("label", self)
        lb.setText("new label")
        lb.setAlignment(Qt.AlignmentFlag.AlignCenter) # 只要显示什么什么Flag，引入from PySide6.QtCore import Qt

        mainLayOut.addWidget(lb)
        self.setLayout(mainLayOut)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()