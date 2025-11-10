# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminForm.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_AdminForm(object):
    def setupUi(self, AdminForm):
        if not AdminForm.objectName():
            AdminForm.setObjectName(u"AdminForm")
        AdminForm.resize(520, 420)
        self.verticalLayout = QVBoxLayout(AdminForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_0 = QLabel(AdminForm)
        self.lbl_0.setObjectName(u"lbl_0")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_0)

        self.id_admin = QSpinBox(AdminForm)
        self.id_admin.setObjectName(u"id_admin")
        self.id_admin.setEnabled(False)
        self.id_admin.setMaximum(2147483647)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_admin)

        self.lbl_1 = QLabel(AdminForm)
        self.lbl_1.setObjectName(u"lbl_1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_1)

        self.username = QLineEdit(AdminForm)
        self.username.setObjectName(u"username")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.username)

        self.lbl_2 = QLabel(AdminForm)
        self.lbl_2.setObjectName(u"lbl_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_2)

        self.password = QLineEdit(AdminForm)
        self.password.setObjectName(u"password")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.password)

        self.lbl_3 = QLabel(AdminForm)
        self.lbl_3.setObjectName(u"lbl_3")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_3)

        self.nama_admin = QLineEdit(AdminForm)
        self.nama_admin.setObjectName(u"nama_admin")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.nama_admin)

        self.lbl_4 = QLabel(AdminForm)
        self.lbl_4.setObjectName(u"lbl_4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_4)

        self.level = QComboBox(AdminForm)
        self.level.addItem("")
        self.level.setObjectName(u"level")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.level)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSave = QPushButton(AdminForm)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClear = QPushButton(AdminForm)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonLayout.addWidget(self.btnClear)

        self.hspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.hspacer)

        self.btnClose = QPushButton(AdminForm)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(AdminForm)

        QMetaObject.connectSlotsByName(AdminForm)
    # setupUi

    def retranslateUi(self, AdminForm):
        AdminForm.setWindowTitle(QCoreApplication.translate("AdminForm", u"Form Admin (Sederhana)", None))
        self.lbl_0.setText(QCoreApplication.translate("AdminForm", u"Id Admin", None))
        self.lbl_1.setText(QCoreApplication.translate("AdminForm", u"Username", None))
        self.lbl_2.setText(QCoreApplication.translate("AdminForm", u"Password", None))
        self.lbl_3.setText(QCoreApplication.translate("AdminForm", u"Nama Admin", None))
        self.lbl_4.setText(QCoreApplication.translate("AdminForm", u"Level", None))
        self.level.setItemText(0, QCoreApplication.translate("AdminForm", u"admin", None))

        self.btnSave.setText(QCoreApplication.translate("AdminForm", u"Simpan", None))
        self.btnClear.setText(QCoreApplication.translate("AdminForm", u"Bersihkan", None))
        self.btnClose.setText(QCoreApplication.translate("AdminForm", u"Tutup", None))
    # retranslateUi

