# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_2.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)
from pathlib import Path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(571, 441)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(67, 30, 271, 41))
        self.label.setPixmap(QPixmap(str(Path(__file__).resolve().parent / "dronedogs_order_form_title_text.png")))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 40, 161, 121))
        self.label_2.setPixmap(QPixmap(str(Path(__file__).resolve().parent / "DroneDogsLogo.png")))
        self.label_2.setScaledContents(True)
        self.label_firstname = QLabel(Dialog)
        self.label_firstname.setObjectName(u"label_firstname")
        self.label_firstname.setGeometry(QRect(128, 205, 71, 21))
        self.label_email = QLabel(Dialog)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(128, 285, 71, 21))
        self.label_lastname = QLabel(Dialog)
        self.label_lastname.setObjectName(u"label_lastname")
        self.label_lastname.setGeometry(QRect(128, 245, 71, 21))
        self.pushButton_addcustomer = QPushButton(Dialog)
        self.pushButton_addcustomer.setObjectName(u"pushButton_addcustomer")
        self.pushButton_addcustomer.setGeometry(QRect(127, 370, 101, 26))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 370, 111, 26))
        self.lineEdit_firstname = QLineEdit(Dialog)
        self.lineEdit_firstname.setObjectName(u"lineEdit_firstname")
        self.lineEdit_firstname.setGeometry(QRect(230, 200, 171, 26))
        self.lineEdit_lastname = QLineEdit(Dialog)
        self.lineEdit_lastname.setObjectName(u"lineEdit_lastname")
        self.lineEdit_lastname.setGeometry(QRect(230, 240, 171, 26))
        self.lineEdit_email = QLineEdit(Dialog)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(230, 280, 171, 26))
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(80, 70, 256, 101))
        self.listWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        QWidget.setTabOrder(self.listWidget, self.lineEdit_firstname)
        QWidget.setTabOrder(self.lineEdit_firstname, self.lineEdit_lastname)
        QWidget.setTabOrder(self.lineEdit_lastname, self.lineEdit_email)
        QWidget.setTabOrder(self.lineEdit_email, self.pushButton_addcustomer)
        QWidget.setTabOrder(self.pushButton_addcustomer, self.pushButton_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_firstname.setText(QCoreApplication.translate("Dialog", u"First Name:", None))
        self.label_email.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_lastname.setText(QCoreApplication.translate("Dialog", u"Last Name:", None))
        self.pushButton_addcustomer.setText(QCoreApplication.translate("Dialog", u"Add Customer", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Select Customer", None))
    # retranslateUi

