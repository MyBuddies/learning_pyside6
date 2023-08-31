from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QLineEdit
)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        # getOpenFileName() 打开一个文件
        # getOpenFileNames() 打开多个文件
        # getExistingDirectory() 打开一个文件夹
        # getSaveFileName() 保存一个文件

        btn = QPushButton('选择打开一个文件')
        '''参数
        -- self 窗体类型
        -- 对话框标题
        -- 打开文件的路径 '.'表示当前路径
        -- 过滤文件 All Files (*);;py文件(*.py *.pyd)
        '''
        btn.clicked.connect(lambda:print(QFileDialog.getOpenFileName(self, '选择文件这是标题', '.', 'All Files (*);;py文件(*.py *.pyd)')))

        btn2 = QPushButton('选择打开多个文件') # 返回值是一个文件绝对路径的字符串列表
        btn2.clicked.connect(lambda:print(QFileDialog.getOpenFileNames(self, '选择文件这是标题', '.', 'All Files (*);;py文件(*.py *.pyd)')))

        btn3 = QPushButton('选择文件夹') # 返回值是一个文件夹绝对路径的字符串
        btn3.clicked.connect(lambda:print(QFileDialog.getExistingDirectory(self, '选择文件夹这是标题', '.')))

        btn4 = QPushButton('保存文件')
        btn4.clicked.connect(lambda:print(QFileDialog.getSaveFileName(self, '选择文件夹这是标题', '.', 'All Files (*);;py文件(*.py *.pyd)')))


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(btn)
        mainLayout.addWidget(btn2)
        mainLayout.addWidget(btn3)
        mainLayout.addWidget(btn4)
        self.setLayout(mainLayout)

       


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

