from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMessageBox
)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)


        self.btn = QPushButton("按钮")
        self.btn.clicked.connect(self.btnClicked)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

    def btnClicked(self):
        # 按照使用场景的频率排列如下：
        # QMessageBox.information(self, '你好', '你好，世界！')
        # 内容，标题，按钮组，默认按钮 OK
        reply = QMessageBox.information(self, '标题', '内容', 
                                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Apply, 
                                QMessageBox.StandardButton.Ok)

        if reply == QMessageBox.StandardButton.Ok:
            print('clicked OK')
        elif reply == QMessageBox.StandardButton.No:
            print('clicked NO')
        elif reply == QMessageBox.StandardButton.Discard:
            print('clicked Discard')
        elif reply == QMessageBox.StandardButton.Apply:
            print('clicked Apply')

            
        # QMessageBox.question(self, '你好', '你好，世界！')
        # QMessageBox.warning(self, '你好', '你好，世界！')
        # QMessageBox.critical(self, '你好', '你好，世界！')
        # QMessageBox.about(self, '你好', '你好，世界！')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

