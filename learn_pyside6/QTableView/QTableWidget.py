from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from faker import Faker

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        self.faker = Faker(locale='zh_CN')
        self.data = [[self.faker.name(), self.faker.address(), self.faker.ascii_free_email()] for _ in range(100)]

        # 创建模型
        self.model = QStandardItemModel()
        for indexRow, row in enumerate(self.data):
            for indexColumn, column in enumerate(row):
                self.model.setItem(indexRow, indexColumn, QStandardItem(column))

        # 创建视图层
        self.tableView =QTableView()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # 设置表格随窗口变化而变化
        self.tableView.setModel(self.model)

        self.tableView.setSortingEnabled(True) # 设置表格排序

        self.tableView.setEditTriggers(QTableView.EditTrigger.NoEditTriggers) # 不能编辑表格
        self.tableView.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows) # 选择每行

        self.tableView2 =QTableView()
        self.tableView2.setModel(self.model)


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.tableView)
        # self.mainLayout.addWidget(self.tableView2)
        self.setLayout(self.mainLayout)




if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()  