# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 340)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnBaptis = QPushButton(self.centralwidget)
        self.btnBaptis.setObjectName(u"btnBaptis")

        self.verticalLayout.addWidget(self.btnBaptis)

        self.btnJadwalIbadah = QPushButton(self.centralwidget)
        self.btnJadwalIbadah.setObjectName(u"btnJadwalIbadah")

        self.verticalLayout.addWidget(self.btnJadwalIbadah)

        self.btnJemaat = QPushButton(self.centralwidget)
        self.btnJemaat.setObjectName(u"btnJemaat")

        self.verticalLayout.addWidget(self.btnJemaat)

        self.btnPengumuman = QPushButton(self.centralwidget)
        self.btnPengumuman.setObjectName(u"btnPengumuman")

        self.verticalLayout.addWidget(self.btnPengumuman)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btnBaptis.setText(QCoreApplication.translate("MainWindow", u"Baptis", None))
        self.btnJadwalIbadah.setText(QCoreApplication.translate("MainWindow", u"Jadwal Ibadah", None))
        self.btnJemaat.setText(QCoreApplication.translate("MainWindow", u"Jemaat", None))
        self.btnPengumuman.setText(QCoreApplication.translate("MainWindow", u"Pengumuman", None))
    # retranslateUi

