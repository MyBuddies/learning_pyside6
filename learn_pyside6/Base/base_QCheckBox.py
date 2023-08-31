from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QCheckBox("是否被选中")
        cb.stateChanged.connect(self.showState) # 选中是2 状态为TRUE；未选中是0 状态为FALSE

        btn = QPushButton("获取状态")
        btn.clicked.connect(lambda:print(cb.isChecked()))

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        mainlayout.addWidget(btn)
        self.setLayout(mainlayout)

    def showName(self, name):
        print(name)

    def showState(self, state):
        print(state)
    
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()