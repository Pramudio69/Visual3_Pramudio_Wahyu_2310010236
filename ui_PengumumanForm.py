# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PengumumanForm.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_PengumumanForm(object):
    def setupUi(self, PengumumanForm):
        if not PengumumanForm.objectName():
            PengumumanForm.setObjectName(u"PengumumanForm")
        PengumumanForm.resize(520, 420)
        self.verticalLayout = QVBoxLayout(PengumumanForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_0 = QLabel(PengumumanForm)
        self.lbl_0.setObjectName(u"lbl_0")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_0)

        self.id_pengumuman = QSpinBox(PengumumanForm)
        self.id_pengumuman.setObjectName(u"id_pengumuman")
        self.id_pengumuman.setEnabled(False)
        self.id_pengumuman.setMaximum(2147483647)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_pengumuman)

        self.lbl_1 = QLabel(PengumumanForm)
        self.lbl_1.setObjectName(u"lbl_1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_1)

        self.sub_jenis = QLineEdit(PengumumanForm)
        self.sub_jenis.setObjectName(u"sub_jenis")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sub_jenis)

        self.lbl_2 = QLabel(PengumumanForm)
        self.lbl_2.setObjectName(u"lbl_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_2)

        self.isi_pengumuman = QLineEdit(PengumumanForm)
        self.isi_pengumuman.setObjectName(u"isi_pengumuman")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.isi_pengumuman)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSave = QPushButton(PengumumanForm)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClear = QPushButton(PengumumanForm)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonLayout.addWidget(self.btnClear)

        self.hspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.hspacer)

        self.btnClose = QPushButton(PengumumanForm)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(PengumumanForm)

        QMetaObject.connectSlotsByName(PengumumanForm)
    # setupUi

    def retranslateUi(self, PengumumanForm):
        PengumumanForm.setWindowTitle(QCoreApplication.translate("PengumumanForm", u"Form Pengumuman (Sederhana)", None))
        self.lbl_0.setText(QCoreApplication.translate("PengumumanForm", u"Id Pengumuman", None))
        self.lbl_1.setText(QCoreApplication.translate("PengumumanForm", u"Sub Jenis", None))
        self.lbl_2.setText(QCoreApplication.translate("PengumumanForm", u"Isi Pengumuman", None))
        self.btnSave.setText(QCoreApplication.translate("PengumumanForm", u"Simpan", None))
        self.btnClear.setText(QCoreApplication.translate("PengumumanForm", u"Bersihkan", None))
        self.btnClose.setText(QCoreApplication.translate("PengumumanForm", u"Tutup", None))
    # retranslateUi

