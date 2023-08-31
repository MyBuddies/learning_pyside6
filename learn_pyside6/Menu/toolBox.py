from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QWidget, QToolBox, QLabel, QPushButton, QStyle


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,400)

        self.toolBox = QToolBox()

        # 创建一个右箭头图标和一个下箭头图标
        self.arrowRight = self.style().standardPixmap(QStyle.StandardPixmap.SP_ArrowRight)
        self.arrowDown = self.style().standardPixmap(QStyle.StandardPixmap.SP_ArrowDown)

        # 创建折叠选项卡内容
        self.widget1 = QWidget()
        self.widget1Layout = QVBoxLayout()
        self.widget1Layout.addWidget(QLabel('这是第一个选项卡'))
        self.widget1Layout.addWidget(QPushButton('按钮1'))
        self.widget1.setLayout(self.widget1Layout)

        self.widget2 = QWidget()
        self.widget2Layout = QVBoxLayout()
        self.widget2Layout.addWidget(QLabel('这是第二个选项卡'))
        self.widget2Layout.addWidget(QPushButton('按钮2'))
        self.widget2.setLayout(self.widget2Layout)

        self.widget3 = QWidget()
        self.widget3Layout = QVBoxLayout()
        self.widget3Layout.addWidget(QLabel('这是第三个选项卡'))
        self.widget3Layout.addWidget(QPushButton('按钮3'))
        self.widget3.setLayout(self.widget3Layout)


        self.toolBox.addItem(self.widget1, self.arrowRight, '选项卡1')
        self.toolBox.addItem(self.widget2, self.arrowRight, '选项卡2')
        self.toolBox.addItem(self.widget3, self.arrowRight, '选项卡3')

        self.toolBox.currentChanged.connect(self.onCurrentChanged)


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.toolBox)
        self.setLayout(self.mainLayout)


    def onCurrentChanged(self, index):
        # 全部重置为向右箭头
        for i in range(self.toolBox.count()):
            self.toolBox.setItemIcon(i, self.arrowRight)

        self.toolBox.setItemIcon(index, self.arrowDown)
        

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()