from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QMenu
from PySide6.QtGui import QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,400)

        self.menu = self.menuBar() # 在QMainWindow自带布局，self.menuBar()
        
        self.openFile = QAction('打开文件')
        self.closeFile = QAction('关闭文件')

        # QAction → QMenu
        # self.Qmenu.addAction(self.QAction)
        self.fileMenu = QMenu('文件')
        self.fileMenu.addAction(self.openFile)
        self.fileMenu.addAction(self.closeFile)

        # 子菜单
        self.moreMenu = QMenu('更多')
        self.moreMenu1 = QAction('更多1')
        self.moreMenu.addAction(self.moreMenu1)
        self.moreMenu2 = QAction('更多2')
        self.moreMenu.addAction(self.moreMenu2)
        self.fileMenu.addMenu(self.moreMenu)

        # Qmenu → QMenuBar
        # self.MenuBar.addMenu(self.Qmenu)
        # 在QMainWindow自带布局，self.menuBar()，不需要创建QMenuBar
        self.menu.addMenu(self.fileMenu)

        self.openFile.triggered.connect(lambda:print('打开文件'))
        self.closeFile.triggered.connect(lambda:print('关闭文件'))
        self.moreMenu1.triggered.connect(lambda:print('more1'))
        self.moreMenu2.triggered.connect(lambda:print('more2'))

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()