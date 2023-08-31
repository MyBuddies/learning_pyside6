from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QSlider,
    QLabel
)
from PySide6.QtCore import Qt
from PIL import Image, ImageFilter, ImageQt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton('点我导入图像')
        self.btn.clicked.connect(self.getImg)

        self.lbShowImg = QLabel()
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 20)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(3)
        self.slider.valueChanged.connect(self.sliderValueChanged)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.lbShowImg)
        self.mainLayout.addWidget(self.slider)
        self.setLayout(self.mainLayout)

    def getImg(self):
        self.img = Image.open(QFileDialog.getOpenFileName(self, '选择图像', './', '图像文件(*.png *.jpg *.jpeg)')[0])
        self.lbShowImg.setPixmap(ImageQt.toqpixmap(self.img))

    def sliderValueChanged(self, value):
        self.blurImg = self.img.filter(ImageFilter.GaussianBlur(value))
        self.lbShowImg.setPixmap(ImageQt.toqpixmap(self.blurImg))


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

