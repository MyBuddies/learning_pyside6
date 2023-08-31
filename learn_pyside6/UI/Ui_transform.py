# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transform.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(328, 259)
        Form.setStyleSheet(u".QComboBox{\n"
"	border-radius:10%;\n"
"	border:1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius:10%;\n"
"	border:1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.dataTypeComboBox = QComboBox(Form)
        self.dataTypeComboBox.setObjectName(u"dataTypeComboBox")
        self.dataTypeComboBox.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.dataTypeComboBox, 2, 0, 1, 1)

        self.twoInputlineEdit = QLineEdit(Form)
        self.twoInputlineEdit.setObjectName(u"twoInputlineEdit")
        self.twoInputlineEdit.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.twoInputlineEdit, 4, 0, 1, 1)

        self.oneInputcomboBox = QComboBox(Form)
        self.oneInputcomboBox.setObjectName(u"oneInputcomboBox")
        self.oneInputcomboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.oneInputcomboBox, 3, 1, 1, 1)

        self.originDataLabel = QLabel(Form)
        self.originDataLabel.setObjectName(u"originDataLabel")
        self.originDataLabel.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(16)
        self.originDataLabel.setFont(font)
        self.originDataLabel.setStyleSheet(u"color: rgb(160, 160, 160);")

        self.gridLayout.addWidget(self.originDataLabel, 0, 0, 1, 1)

        self.twoInputcomboBox = QComboBox(Form)
        self.twoInputcomboBox.setObjectName(u"twoInputcomboBox")
        self.twoInputcomboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.twoInputcomboBox, 4, 1, 1, 1)

        self.transDataLabel = QLabel(Form)
        self.transDataLabel.setObjectName(u"transDataLabel")
        self.transDataLabel.setMinimumSize(QSize(200, 0))
        self.transDataLabel.setMaximumSize(QSize(400, 80))
        font1 = QFont()
        font1.setPointSize(29)
        self.transDataLabel.setFont(font1)

        self.gridLayout.addWidget(self.transDataLabel, 1, 0, 1, 1)

        self.oneInputlineEdit = QLineEdit(Form)
        self.oneInputlineEdit.setObjectName(u"oneInputlineEdit")
        self.oneInputlineEdit.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.oneInputlineEdit, 3, 0, 1, 1)

        self.calBtn = QPushButton(Form)
        self.calBtn.setObjectName(u"calBtn")

        self.gridLayout.addWidget(self.calBtn, 5, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8fdb\u5236\u8f6c\u6362\u5668", None))
        self.originDataLabel.setText(QCoreApplication.translate("Form", u"0=", None))
        self.transDataLabel.setText(QCoreApplication.translate("Form", u"0", None))
        self.calBtn.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
    # retranslateUi

