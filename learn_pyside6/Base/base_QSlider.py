from PySide6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        slider = QSlider(Qt.Orientation.Horizontal) # 设置滑条为水平，from PySide6.QtCore import Qt
        slider.setTickPosition(QSlider.TickPosition.TicksBelow) # 设置刻度的位置
        slider.setTickInterval(5) # 设置刻度的间隔
        # 设置最小值和最大值
        slider.setMaximum(150)
        slider.setMinimum(50)

        slider.valueChanged.connect(self.showSlider)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(slider)
        self.setLayout(mainLayout)
    
    def showSlider(self):
        current_widget = self.sender()
        print(current_widget.value())
    
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()