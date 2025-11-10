# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BaptisForm.ui'
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

class Ui_BaptisForm(object):
    def setupUi(self, BaptisForm):
        if not BaptisForm.objectName():
            BaptisForm.setObjectName(u"BaptisForm")
        BaptisForm.resize(560, 420)
        self.verticalLayout = QVBoxLayout(BaptisForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_id_baptis = QLabel(BaptisForm)
        self.label_id_baptis.setObjectName(u"label_id_baptis")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_id_baptis)

        self.id_baptis = QSpinBox(BaptisForm)
        self.id_baptis.setObjectName(u"id_baptis")
        self.id_baptis.setEnabled(False)
        self.id_baptis.setMaximum(2147483647)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_baptis)

        self.label_id_jemaat = QLabel(BaptisForm)
        self.label_id_jemaat.setObjectName(u"label_id_jemaat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_id_jemaat)

        self.id_jemaat = QComboBox(BaptisForm)
        self.id_jemaat.setObjectName(u"id_jemaat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.id_jemaat)

        self.label_nama_ayah = QLabel(BaptisForm)
        self.label_nama_ayah.setObjectName(u"label_nama_ayah")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_nama_ayah)

        self.nama_ayah = QLineEdit(BaptisForm)
        self.nama_ayah.setObjectName(u"nama_ayah")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.nama_ayah)

        self.label_nama_ibu = QLabel(BaptisForm)
        self.label_nama_ibu.setObjectName(u"label_nama_ibu")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_nama_ibu)

        self.nama_ibu = QLineEdit(BaptisForm)
        self.nama_ibu.setObjectName(u"nama_ibu")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.nama_ibu)

        self.label_nama_wali = QLabel(BaptisForm)
        self.label_nama_wali.setObjectName(u"label_nama_wali")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_nama_wali)

        self.nama_wali = QLineEdit(BaptisForm)
        self.nama_wali.setObjectName(u"nama_wali")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.nama_wali)

        self.label_tgl_baptis = QLabel(BaptisForm)
        self.label_tgl_baptis.setObjectName(u"label_tgl_baptis")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_tgl_baptis)

        self.tgl_baptis = QDateEdit(BaptisForm)
        self.tgl_baptis.setObjectName(u"tgl_baptis")
        self.tgl_baptis.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.tgl_baptis)

        self.label_pelayan = QLabel(BaptisForm)
        self.label_pelayan.setObjectName(u"label_pelayan")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_pelayan)

        self.pelayan = QLineEdit(BaptisForm)
        self.pelayan.setObjectName(u"pelayan")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.pelayan)

        self.label_surat_baptis = QLabel(BaptisForm)
        self.label_surat_baptis.setObjectName(u"label_surat_baptis")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_surat_baptis)

        self.surat_baptis = QLineEdit(BaptisForm)
        self.surat_baptis.setObjectName(u"surat_baptis")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.surat_baptis)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSave = QPushButton(BaptisForm)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClear = QPushButton(BaptisForm)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonLayout.addWidget(self.btnClear)

        self.hspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.hspacer)

        self.btnClose = QPushButton(BaptisForm)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(BaptisForm)

        QMetaObject.connectSlotsByName(BaptisForm)
    # setupUi

    def retranslateUi(self, BaptisForm):
        BaptisForm.setWindowTitle(QCoreApplication.translate("BaptisForm", u"BaptisForm (Sederhana)", None))
        self.label_id_baptis.setText(QCoreApplication.translate("BaptisForm", u"Id Baptis", None))
        self.label_id_jemaat.setText(QCoreApplication.translate("BaptisForm", u"Id Jemaat", None))
        self.label_nama_ayah.setText(QCoreApplication.translate("BaptisForm", u"Nama Ayah", None))
        self.label_nama_ibu.setText(QCoreApplication.translate("BaptisForm", u"Nama Ibu", None))
        self.label_nama_wali.setText(QCoreApplication.translate("BaptisForm", u"Nama Wali", None))
        self.label_tgl_baptis.setText(QCoreApplication.translate("BaptisForm", u"Tgl Baptis", None))
        self.label_pelayan.setText(QCoreApplication.translate("BaptisForm", u"Pelayan", None))
        self.label_surat_baptis.setText(QCoreApplication.translate("BaptisForm", u"Surat Baptis", None))
        self.btnSave.setText(QCoreApplication.translate("BaptisForm", u"Simpan", None))
        self.btnClear.setText(QCoreApplication.translate("BaptisForm", u"Bersihkan", None))
        self.btnClose.setText(QCoreApplication.translate("BaptisForm", u"Tutup", None))
    # retranslateUi

