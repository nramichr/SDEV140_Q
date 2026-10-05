# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DroneDogs.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_DroneDogs(object):
    def setupUi(self, DroneDogs):
        if not DroneDogs.objectName():
            DroneDogs.setObjectName(u"DroneDogs")
        DroneDogs.resize(854, 627)
        self.centralwidget = QWidget(DroneDogs)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LabeTitle = QLabel(self.centralwidget)
        self.LabeTitle.setObjectName(u"LabeTitle")
        self.LabeTitle.setGeometry(QRect(90, 30, 341, 91))
        self.LabeTitle.setPixmap(QPixmap(u"../../../dronedogs_order_form_title_text.png"))
        self.LabeTitle.setScaledContents(True)
        self.LabelLogo = QLabel(self.centralwidget)
        self.LabelLogo.setObjectName(u"LabelLogo")
        self.LabelLogo.setGeometry(QRect(490, 60, 231, 201))
        self.LabelLogo.setPixmap(QPixmap(u"../../../DroneDogsLogo.png"))
        self.LabelLogo.setScaledContents(True)
        self.Label_BeefDogs = QLabel(self.centralwidget)
        self.Label_BeefDogs.setObjectName(u"Label_BeefDogs")
        self.Label_BeefDogs.setGeometry(QRect(50, 130, 81, 20))
        self.Label_Subtotal = QLabel(self.centralwidget)
        self.Label_Subtotal.setObjectName(u"Label_Subtotal")
        self.Label_Subtotal.setGeometry(QRect(90, 390, 51, 21))
        self.Label_Sales_Tax = QLabel(self.centralwidget)
        self.Label_Sales_Tax.setObjectName(u"Label_Sales_Tax")
        self.Label_Sales_Tax.setGeometry(QRect(90, 450, 49, 16))
        self.Label_total_cost = QLabel(self.centralwidget)
        self.Label_total_cost.setObjectName(u"Label_total_cost")
        self.Label_total_cost.setGeometry(QRect(80, 505, 61, 21))
        self.Spin_Box__BeefDogs = QSpinBox(self.centralwidget)
        self.Spin_Box__BeefDogs.setObjectName(u"Spin_Box__BeefDogs")
        self.Spin_Box__BeefDogs.setGeometry(QRect(160, 130, 131, 26))
        self.Spin_Box__PorkDogs = QSpinBox(self.centralwidget)
        self.Spin_Box__PorkDogs.setObjectName(u"Spin_Box__PorkDogs")
        self.Spin_Box__PorkDogs.setGeometry(QRect(160, 180, 131, 26))
        self.Spin_Box__TurkeyDogs = QSpinBox(self.centralwidget)
        self.Spin_Box__TurkeyDogs.setObjectName(u"Spin_Box__TurkeyDogs")
        self.Spin_Box__TurkeyDogs.setGeometry(QRect(160, 230, 131, 26))
        self.Label_PorkDogs = QLabel(self.centralwidget)
        self.Label_PorkDogs.setObjectName(u"Label_PorkDogs")
        self.Label_PorkDogs.setGeometry(QRect(50, 180, 81, 20))
        self.Label_TurkeyDogs = QLabel(self.centralwidget)
        self.Label_TurkeyDogs.setObjectName(u"Label_TurkeyDogs")
        self.Label_TurkeyDogs.setGeometry(QRect(40, 230, 91, 20))
        self.lineEdit_Subtotal = QLineEdit(self.centralwidget)
        self.lineEdit_Subtotal.setObjectName(u"lineEdit_Subtotal")
        self.lineEdit_Subtotal.setEnabled(False)
        self.lineEdit_Subtotal.setGeometry(QRect(160, 390, 113, 26))
        self.lineEdit_Subtotal.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_Subtotal.setReadOnly(True)
        self.lineEdit_2_Sales_Tax = QLineEdit(self.centralwidget)
        self.lineEdit_2_Sales_Tax.setObjectName(u"lineEdit_2_Sales_Tax")
        self.lineEdit_2_Sales_Tax.setEnabled(False)
        self.lineEdit_2_Sales_Tax.setGeometry(QRect(160, 450, 113, 26))
        self.lineEdit_2_Sales_Tax.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_2_Sales_Tax.setReadOnly(True)
        self.lineEdit_3_Total_cost = QLineEdit(self.centralwidget)
        self.lineEdit_3_Total_cost.setObjectName(u"lineEdit_3_Total_cost")
        self.lineEdit_3_Total_cost.setEnabled(False)
        self.lineEdit_3_Total_cost.setGeometry(QRect(160, 500, 113, 26))
        self.lineEdit_3_Total_cost.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_3_Total_cost.setReadOnly(True)
        self.pushButton_calculate_order = QPushButton(self.centralwidget)
        self.pushButton_calculate_order.setObjectName(u"pushButton_calculate_order")
        self.pushButton_calculate_order.setGeometry(QRect(140, 310, 125, 26))
        self.pushButton_2_Submit_order = QPushButton(self.centralwidget)
        self.pushButton_2_Submit_order.setObjectName(u"pushButton_2_Submit_order")
        self.pushButton_2_Submit_order.setGeometry(QRect(340, 310, 125, 26))
        self.pushButton_3_Exit = QPushButton(self.centralwidget)
        self.pushButton_3_Exit.setObjectName(u"pushButton_3_Exit")
        self.pushButton_3_Exit.setGeometry(QRect(550, 310, 125, 26))
        DroneDogs.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DroneDogs)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 854, 33))
        DroneDogs.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DroneDogs)
        self.statusbar.setObjectName(u"statusbar")
        DroneDogs.setStatusBar(self.statusbar)

        self.retranslateUi(DroneDogs)

        QMetaObject.connectSlotsByName(DroneDogs)
    # setupUi

    def retranslateUi(self, DroneDogs):
        DroneDogs.setWindowTitle(QCoreApplication.translate("DroneDogs", u"MainWindow", None))
        self.LabeTitle.setText("")
        self.LabelLogo.setText("")
        self.Label_BeefDogs.setText(QCoreApplication.translate("DroneDogs", u"# of Beef Dogs", None))
        self.Label_Subtotal.setText(QCoreApplication.translate("DroneDogs", u"Subtotal:", None))
        self.Label_Sales_Tax.setText(QCoreApplication.translate("DroneDogs", u"Sales Tax:", None))
        self.Label_total_cost.setText(QCoreApplication.translate("DroneDogs", u"Total Cost:", None))
        self.Label_PorkDogs.setText(QCoreApplication.translate("DroneDogs", u"# of Pork Dogs", None))
        self.Label_TurkeyDogs.setText(QCoreApplication.translate("DroneDogs", u"# of Turkey Dogs", None))
        self.pushButton_calculate_order.setText(QCoreApplication.translate("DroneDogs", u"Calculate Order", None))
        self.pushButton_2_Submit_order.setText(QCoreApplication.translate("DroneDogs", u"Submit Order", None))
        self.pushButton_3_Exit.setText(QCoreApplication.translate("DroneDogs", u"Exit", None))
    # retranslateUi

