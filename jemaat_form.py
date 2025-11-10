# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader
import crud

def load_ui(path):
    f = QFile(path); f.open(QFile.ReadOnly)
    w = QUiLoader().load(f); f.close()
    return w

def msg(parent, text):
    QMessageBox.information(parent, "Info", text)

class JemaatForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = load_ui("JemaatForm.ui")
        self.w.setParent(self)
        self.w.setWindowTitle("JemaatForm (Sederhana)")
        self.w.btnSave.clicked.connect(self.on_save)
        self.w.btnClear.clicked.connect(self.on_clear)
        self.w.btnClose.clicked.connect(self.close)

    def _collect_data(self):
        data = {}
        data["id_jemaat"] = self.w.id_jemaat.value()
        data["nama_jemaat"] = self.w.nama_jemaat.text() if hasattr(self.w, "nama_jemaat") else ""
        data["jk_jemaat"] = self.w.jk_jemaat.currentText() if hasattr(self.w, "jk_jemaat") else None
        data["alamat_jemaat"] = self.w.alamat_jemaat.text() if hasattr(self.w, "alamat_jemaat") else ""
        data["tempat_lahir"] = self.w.tempat_lahir.text() if hasattr(self.w, "tempat_lahir") else ""
        data["tgl_lahir"] = self.w.tgl_lahir.date().toString("yyyy-MM-dd") if hasattr(self.w, "tgl_lahir") else None
        data["no_hp"] = self.w.no_hp.text() if hasattr(self.w, "no_hp") else ""
        data["status_dalam_keluarga"] = self.w.status_dalam_keluarga.text() if hasattr(self.w, "status_dalam_keluarga") else ""
        data["wilayah"] = self.w.wilayah.text() if hasattr(self.w, "wilayah") else ""
        return data

    def on_clear(self):
        self.w.id_jemaat.setValue(0)
        (self.w.nama_jemaat.clear() if hasattr(self.w, "nama_jemaat") else None)
        (self.w.jk_jemaat.setCurrentIndex(0) if hasattr(self.w, "jk_jemaat") else None)
        (self.w.alamat_jemaat.clear() if hasattr(self.w, "alamat_jemaat") else None)
        (self.w.tempat_lahir.clear() if hasattr(self.w, "tempat_lahir") else None)
        (self.w.tgl_lahir.setDate(QDate.currentDate()) if hasattr(self.w, "tgl_lahir") else None)
        (self.w.no_hp.clear() if hasattr(self.w, "no_hp") else None)
        (self.w.status_dalam_keluarga.clear() if hasattr(self.w, "status_dalam_keluarga") else None)
        (self.w.wilayah.clear() if hasattr(self.w, "wilayah") else None)
        msg(self, "Form dibersihkan.")

    def on_save(self):
        data = self._collect_data()
        pk_val = data.get("id_jemaat", 0)
        try:
            if not pk_val:
                new_id = getattr(crud, "jemaat_insert")(data)
                if hasattr(self.w, "id_jemaat"):
                    self.w.id_jemaat.setValue(new_id)
                msg(self, f"Data berhasil ditambahkan (ID: {new_id})")
            else:
                data.pop("id_jemaat", None)
                rows = getattr(crud, "jemaat_update")(pk_val, data)
                msg(self, f"Perubahan disimpan ({rows} baris).")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show(self):
        self.w.show()
