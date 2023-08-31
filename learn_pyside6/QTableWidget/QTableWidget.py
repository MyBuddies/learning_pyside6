from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
from faker import Faker

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        self.faker = Faker(locale='zh_CN')
        self.data = [[self.faker.name(), self.faker.address(), self.faker.ascii_free_email()] for _ in range(80)]

        self.table = QTableWidget()
        self.table.setRowCount(80)
        self.table.setColumnCount(3)

        # 设置表头
        self.table.setHorizontalHeaderLabels(['姓名', '地址', '邮箱'])
        # 设置表格随窗口变化而变化
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for rowIndex, row in enumerate(self.data): # 拿出每行的元素存在row里，rowIndex存行下标
            for columnIndex, item in enumerate(row): # 对于拿出的每行的元素row，columIndex存列下标，对应下标的元素为item
                self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(item))


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.table)
        self.setLayout(self.mainLayout)




if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()  