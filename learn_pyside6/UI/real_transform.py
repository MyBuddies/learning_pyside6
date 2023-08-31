from PySide6.QtWidgets import QApplication, QWidget
from Ui_transform import Ui_Form # 第一，导入

class MyWindow(QWidget, Ui_Form): # 第二，继承
    def __init__(self):
        super().__init__()

        self.setupUi(self) # 第三，执行

        # 用于存储数据类型的字典
        self.lengthVar = {"厘米":1, "分米":10, "米":100, "千米":100000}
        self.weightVar = {"克":1, "千克":1000, "斤":500}

        self.TypeDict = {"长度":self.lengthVar, "质量":self.weightVar}

        self.dataTypeComboBox.addItems(self.TypeDict.keys())
        self.oneInputcomboBox.addItems(self.lengthVar.keys())
        self.twoInputcomboBox.addItems(self.lengthVar.keys())
        self.bind()

    def bind(self):
        self.dataTypeComboBox.currentIndexChanged.connect(self.typeChanged)
        self.calBtn.clicked.connect(self.calc)

    def calc(self):
        bigType = self.dataTypeComboBox.currentText()
        # 获取第一个输入框的值
        value = self.oneInputlineEdit.text()
        if value == "":
            return
        
        currentType = self.oneInputcomboBox.currentText()
        transType = self.twoInputcomboBox.currentText()

        standardization = float(value)*self.TypeDict[bigType][transType] # 标准化
        result = standardization / self.TypeDict[bigType][currentType]

        self.originDataLabel.setText(f'{value}{currentType}=')
        self.transDataLabel.setText(f'{result}{transType}')
        self.twoInputlineEdit.setText(str(result))

    def typeChanged(self, text):
        self.oneInputcomboBox.clear()
        self.twoInputcomboBox.clear()
        
        self.oneInputcomboBox.addItems(self.TypeDict[text].keys())
        self.twoInputcomboBox.addItems(self.TypeDict[text].keys())





        

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()