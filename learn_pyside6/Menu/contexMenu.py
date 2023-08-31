from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QWidget
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
'''
- 对窗体进行上下文菜单的添加
-- 1.设置窗体的上下文菜单策略   self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
-- 2.创建 QAction   elf.openFile = QAction('打开文件')
-- 3.将QAction添加到窗体中   self.addAction(self.closeFile)
-- 4.绑定逻辑
'''
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,400)

        # 对窗体进行上下文菜单添加
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.openFile = QAction('打开文件')
        self.closeFile = QAction('关闭文件')
        # self.addAction(self.openFile)
        # self.addAction(self.closeFile)
        self.addActions([self.openFile, self.closeFile]) # 注意addAction & addActions

        # 对控件进行上下文菜单添加
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit1.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.sendValue = QAction('把值发送到输入框2')
        self.showCurrentValue = QAction('显示当前值')
        self.lineEdit1.addActions([self.sendValue, self.showCurrentValue])

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEdit1)
        self.mainLayout.addWidget(self.lineEdit2)
        self.setLayout(self.mainLayout)

        self.bind()

    def bind(self):
        self.openFile.triggered.connect(lambda:print('打开文件'))
        self.closeFile.triggered.connect(lambda:print('关闭文件'))
        self.sendValue.triggered.connect(lambda:self.lineEdit2.setText(self.lineEdit1.text()))
        self.showCurrentValue.triggered.connect(lambda:print(self.lineEdit1.text()))

        

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()