# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Jadwal_ibadahForm.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Jadwal_ibadahForm(object):
    def setupUi(self, Jadwal_ibadahForm):
        if not Jadwal_ibadahForm.objectName():
            Jadwal_ibadahForm.setObjectName(u"Jadwal_ibadahForm")
        Jadwal_ibadahForm.resize(520, 420)
        self.verticalLayout = QVBoxLayout(Jadwal_ibadahForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_0 = QLabel(Jadwal_ibadahForm)
        self.lbl_0.setObjectName(u"lbl_0")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_0)

        self.id_jdl_ibadah = QSpinBox(Jadwal_ibadahForm)
        self.id_jdl_ibadah.setObjectName(u"id_jdl_ibadah")
        self.id_jdl_ibadah.setEnabled(False)
        self.id_jdl_ibadah.setMaximum(2147483647)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_jdl_ibadah)

        self.lbl_1 = QLabel(Jadwal_ibadahForm)
        self.lbl_1.setObjectName(u"lbl_1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_1)

        self.id_jemaat = QSpinBox(Jadwal_ibadahForm)
        self.id_jemaat.setObjectName(u"id_jemaat")
        self.id_jemaat.setMaximum(2147483647)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.id_jemaat)

        self.lbl_2 = QLabel(Jadwal_ibadahForm)
        self.lbl_2.setObjectName(u"lbl_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_2)

        self.tgl_ibadah = QDateEdit(Jadwal_ibadahForm)
        self.tgl_ibadah.setObjectName(u"tgl_ibadah")
        self.tgl_ibadah.setCalendarPopup(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.tgl_ibadah)

        self.lbl_3 = QLabel(Jadwal_ibadahForm)
        self.lbl_3.setObjectName(u"lbl_3")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_3)

        self.wilayah = QLineEdit(Jadwal_ibadahForm)
        self.wilayah.setObjectName(u"wilayah")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.wilayah)

        self.lbl_4 = QLabel(Jadwal_ibadahForm)
        self.lbl_4.setObjectName(u"lbl_4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_4)

        self.hari_ibadah = QLineEdit(Jadwal_ibadahForm)
        self.hari_ibadah.setObjectName(u"hari_ibadah")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.hari_ibadah)

        self.lbl_5 = QLabel(Jadwal_ibadahForm)
        self.lbl_5.setObjectName(u"lbl_5")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lbl_5)

        self.jam_ibadah = QLineEdit(Jadwal_ibadahForm)
        self.jam_ibadah.setObjectName(u"jam_ibadah")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.jam_ibadah)

        self.lbl_6 = QLabel(Jadwal_ibadahForm)
        self.lbl_6.setObjectName(u"lbl_6")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lbl_6)

        self.pemimpin_ibadah = QLineEdit(Jadwal_ibadahForm)
        self.pemimpin_ibadah.setObjectName(u"pemimpin_ibadah")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.pemimpin_ibadah)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSave = QPushButton(Jadwal_ibadahForm)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClear = QPushButton(Jadwal_ibadahForm)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonLayout.addWidget(self.btnClear)

        self.hspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.hspacer)

        self.btnClose = QPushButton(Jadwal_ibadahForm)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(Jadwal_ibadahForm)

        QMetaObject.connectSlotsByName(Jadwal_ibadahForm)
    # setupUi

    def retranslateUi(self, Jadwal_ibadahForm):
        Jadwal_ibadahForm.setWindowTitle(QCoreApplication.translate("Jadwal_ibadahForm", u"Form Jadwal Ibadah (Sederhana)", None))
        self.lbl_0.setText(QCoreApplication.translate("Jadwal_ibadahForm", u"Id Jdl Ibadah", None))
        self.lbl_1.setText(QCoreApplication.translate("Jadwal_ibadahForm", u"Id Jemaat", None))
        self.lbl_2.setText(QCoreApplication.translate("Jadwal_ibadahForm", u"Tgl Ibadah", None))
        self.lbl_3.setText(QCoreApplication.translate("Jadwal_ibadahForm", u"Wilayah", None))
        self.lbl_4.setText(QCoreApplication.translate("Jadwal_ibadahForm", u"Hari Ibadah", None))
        self.lbl_5.setText(QCoreApplication.translate("Jadwal_ibadahForm", u"Jam Ibadah", None))
        self.lbl_6.setText(QCoreApplication.translate("Jadwal_ibadahForm", u"Pemimpin Ibadah", None))
        self.btnSave.setText(QCoreApplication.translate("Jadwal_ibadahForm", u"Simpan", None))
        self.btnClear.setText(QCoreApplication.translate("Jadwal_ibadahForm", u"Bersihkan", None))
        self.btnClose.setText(QCoreApplication.translate("Jadwal_ibadahForm", u"Tutup", None))
    # retranslateUi

