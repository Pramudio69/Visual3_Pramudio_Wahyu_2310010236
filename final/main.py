from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from jemaat_form import FormJemaat
from baptis_form import FormBaptis
from jadwal_ibadah_form import FormJadwalIbadah
from pengumuman_form import FormPengumuman

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        UI_FILE = Path(__file__).resolve().parent / "main.ui"
        filenya = QFile(str(UI_FILE))
        if not filenya.open(QFile.ReadOnly):
            raise RuntimeError(f"Gagal membuka UI: {UI_FILE}")

        loader = QUiLoader()
        self._ui = loader.load(filenya, None)
        filenya.close()

        if self._ui is None:
            raise RuntimeError("Gagal load main.ui (hasil loader None)")
        self.resize(self._ui.size())
        self.setWindowTitle(self._ui.windowTitle())
        self.setMenuBar(self._ui.menuBar())
        self.setStatusBar(self._ui.statusBar())
        self.setCentralWidget(self._ui.centralWidget())

        self._ui.actionDATA_JEMAAT.triggered.connect(self.buka_jemaat)
        self._ui.actionDATA_BAPTIS.triggered.connect(self.buka_baptis)
        self._ui.actionJADWAL_IBADAH.triggered.connect(self.buka_jadwal)
        self._ui.actionPENGUMUMAN.triggered.connect(self.buka_pengumuman)

        self._windows = {}

    def buka_jemaat(self):
        self._windows["jemaat"] = FormJemaat()
        self._windows["jemaat"].show()

    def buka_baptis(self):
        self._windows["baptis"] = FormBaptis()
        self._windows["baptis"].show()

    def buka_jadwal(self):
        self._windows["jadwal"] = FormJadwalIbadah()
        self._windows["jadwal"].show()

    def buka_pengumuman(self):
        self._windows["pengumuman"] = FormPengumuman()
        self._windows["pengumuman"].show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = MainWindow()
    jendela.show()
    sys.exit(app.exec())
