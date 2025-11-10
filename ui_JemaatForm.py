# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JemaatForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_JemaatForm(object):
    def setupUi(self, JemaatForm):
        if not JemaatForm.objectName():
            JemaatForm.setObjectName(u"JemaatForm")
        JemaatForm.resize(520, 420)
        self.verticalLayout = QVBoxLayout(JemaatForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_0 = QLabel(JemaatForm)
        self.lbl_0.setObjectName(u"lbl_0")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_0)

        self.id_jemaat = QSpinBox(JemaatForm)
        self.id_jemaat.setObjectName(u"id_jemaat")
        self.id_jemaat.setEnabled(False)
        self.id_jemaat.setMaximum(2147483647)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_jemaat)

        self.lbl_1 = QLabel(JemaatForm)
        self.lbl_1.setObjectName(u"lbl_1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_1)

        self.nama_jemaat = QLineEdit(JemaatForm)
        self.nama_jemaat.setObjectName(u"nama_jemaat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nama_jemaat)

        self.lbl_2 = QLabel(JemaatForm)
        self.lbl_2.setObjectName(u"lbl_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_2)

        self.jk_jemaat = QComboBox(JemaatForm)
        self.jk_jemaat.addItem("")
        self.jk_jemaat.setObjectName(u"jk_jemaat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.jk_jemaat)

        self.lbl_3 = QLabel(JemaatForm)
        self.lbl_3.setObjectName(u"lbl_3")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_3)

        self.alamat_jemaat = QLineEdit(JemaatForm)
        self.alamat_jemaat.setObjectName(u"alamat_jemaat")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.alamat_jemaat)

        self.lbl_4 = QLabel(JemaatForm)
        self.lbl_4.setObjectName(u"lbl_4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_4)

        self.tempat_lahir = QLineEdit(JemaatForm)
        self.tempat_lahir.setObjectName(u"tempat_lahir")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tempat_lahir)

        self.lbl_5 = QLabel(JemaatForm)
        self.lbl_5.setObjectName(u"lbl_5")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lbl_5)

        self.tgl_lahir = QDateEdit(JemaatForm)
        self.tgl_lahir.setObjectName(u"tgl_lahir")
        self.tgl_lahir.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.tgl_lahir)

        self.lbl_6 = QLabel(JemaatForm)
        self.lbl_6.setObjectName(u"lbl_6")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lbl_6)

        self.no_hp = QLineEdit(JemaatForm)
        self.no_hp.setObjectName(u"no_hp")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.no_hp)

        self.lbl_7 = QLabel(JemaatForm)
        self.lbl_7.setObjectName(u"lbl_7")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lbl_7)

        self.status_dalam_keluarga = QLineEdit(JemaatForm)
        self.status_dalam_keluarga.setObjectName(u"status_dalam_keluarga")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.status_dalam_keluarga)

        self.lbl_8 = QLabel(JemaatForm)
        self.lbl_8.setObjectName(u"lbl_8")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lbl_8)

        self.wilayah = QLineEdit(JemaatForm)
        self.wilayah.setObjectName(u"wilayah")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.wilayah)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSave = QPushButton(JemaatForm)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClear = QPushButton(JemaatForm)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonLayout.addWidget(self.btnClear)

        self.hspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.hspacer)

        self.btnClose = QPushButton(JemaatForm)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(JemaatForm)

        QMetaObject.connectSlotsByName(JemaatForm)
    # setupUi

    def retranslateUi(self, JemaatForm):
        JemaatForm.setWindowTitle(QCoreApplication.translate("JemaatForm", u"Form Jemaat (Sederhana)", None))
        self.lbl_0.setText(QCoreApplication.translate("JemaatForm", u"Id Jemaat", None))
        self.lbl_1.setText(QCoreApplication.translate("JemaatForm", u"Nama Jemaat", None))
        self.lbl_2.setText(QCoreApplication.translate("JemaatForm", u"Jk Jemaat", None))
        self.jk_jemaat.setItemText(0, QCoreApplication.translate("JemaatForm", u"l", None))

        self.lbl_3.setText(QCoreApplication.translate("JemaatForm", u"Alamat Jemaat", None))
        self.lbl_4.setText(QCoreApplication.translate("JemaatForm", u"Tempat Lahir", None))
        self.lbl_5.setText(QCoreApplication.translate("JemaatForm", u"Tgl Lahir", None))
        self.lbl_6.setText(QCoreApplication.translate("JemaatForm", u"No Hp", None))
        self.lbl_7.setText(QCoreApplication.translate("JemaatForm", u"Status Dalam Keluarga", None))
        self.lbl_8.setText(QCoreApplication.translate("JemaatForm", u"Wilayah", None))
        self.btnSave.setText(QCoreApplication.translate("JemaatForm", u"Simpan", None))
        self.btnClear.setText(QCoreApplication.translate("JemaatForm", u"Bersihkan", None))
        self.btnClose.setText(QCoreApplication.translate("JemaatForm", u"Tutup", None))
    # retranslateUi

