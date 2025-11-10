# main.py (no 'admin' table)
import os, sys
from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader

from baptis_form import BaptisForm
from jadwal_ibadah_form import Jadwal_ibadahForm
from jemaat_form import JemaatForm
from pengumuman_form import PengumumanForm

def load_ui(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"UI file tidak ditemukan: {path}")
    f = QFile(path)
    if not f.open(QFile.ReadOnly):
        raise RuntimeError(f"Gagal membuka UI: {path}")
    try:
        w = QUiLoader().load(f)
        if w is None:
            raise RuntimeError(f"QUiLoader gagal memuat: {path}")
        return w
    finally:
        f.close()

def connect_btn(root, name: str, handler):
    btn = root.findChild(QPushButton, name)
    if btn is None:
        QMessageBox.critical(root, "Error", f"Tombol '{name}' tidak ditemukan di main.ui")
        return None
    btn.clicked.connect(handler)
    return btn

def show_as_top_level(w):
    if w.parent() is not None:
        w.setParent(None)
    w.setWindowFlag(Qt.Window, True)
    w.show()
    try:
        w.raise_(); w.activateWindow()
    except Exception:
        pass

def open_form(key: str, forms: dict, parent):
    try:
        form = forms[key]
        w = getattr(form, "w", None)
        if w is not None:
            show_as_top_level(w)
        else:
            form.show()
    except Exception as e:
        QMessageBox.critical(parent, "Error", f"Gagal membuka form '{key}': {e}")

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app = QApplication(sys.argv)
    main_win = load_ui("main.ui")

    forms = {
        "baptis": BaptisForm(),
        "jadwal_ibadah": Jadwal_ibadahForm(),
        "jemaat": JemaatForm(),
        "pengumuman": PengumumanForm(),
    }

    connect_btn(main_win, "btnBaptis",      lambda: open_form("baptis", forms, main_win))
    connect_btn(main_win, "btnJadwalIbadah",lambda: open_form("jadwal_ibadah", forms, main_win))
    connect_btn(main_win, "btnJemaat",      lambda: open_form("jemaat", forms, main_win))
    connect_btn(main_win, "btnPengumuman",  lambda: open_form("pengumuman", forms, main_win))

    main_win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
