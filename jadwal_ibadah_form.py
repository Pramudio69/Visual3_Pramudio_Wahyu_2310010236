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

class Jadwal_ibadahForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = load_ui("Jadwal_ibadahForm.ui")
        self.w.setParent(self)
        self.w.setWindowTitle("Jadwal_ibadahForm (Sederhana)")
        self.w.btnSave.clicked.connect(self.on_save)
        self.w.btnClear.clicked.connect(self.on_clear)
        self.w.btnClose.clicked.connect(self.close)

    def _collect_data(self):
        data = {}
        data["id_jdl_ibadah"] = self.w.id_jdl_ibadah.value()
        data["id_jemaat"] = self.w.id_jemaat.value() if hasattr(self.w, "id_jemaat") else 0
        data["tgl_ibadah"] = self.w.tgl_ibadah.date().toString("yyyy-MM-dd") if hasattr(self.w, "tgl_ibadah") else None
        data["wilayah"] = self.w.wilayah.text() if hasattr(self.w, "wilayah") else ""
        data["hari_ibadah"] = self.w.hari_ibadah.text() if hasattr(self.w, "hari_ibadah") else ""
        data["jam_ibadah"] = self.w.jam_ibadah.text() if hasattr(self.w, "jam_ibadah") else ""
        data["pemimpin_ibadah"] = self.w.pemimpin_ibadah.text() if hasattr(self.w, "pemimpin_ibadah") else ""
        return data

    def on_clear(self):
        self.w.id_jdl_ibadah.setValue(0)
        (self.w.id_jemaat.setValue(0) if hasattr(self.w, "id_jemaat") else None)
        (self.w.tgl_ibadah.setDate(QDate.currentDate()) if hasattr(self.w, "tgl_ibadah") else None)
        (self.w.wilayah.clear() if hasattr(self.w, "wilayah") else None)
        (self.w.hari_ibadah.clear() if hasattr(self.w, "hari_ibadah") else None)
        (self.w.jam_ibadah.clear() if hasattr(self.w, "jam_ibadah") else None)
        (self.w.pemimpin_ibadah.clear() if hasattr(self.w, "pemimpin_ibadah") else None)
        msg(self, "Form dibersihkan.")

    def on_save(self):
        data = self._collect_data()
        pk_val = data.get("id_jdl_ibadah", 0)
        try:
            if not pk_val:
                new_id = getattr(crud, "jadwal_ibadah_insert")(data)
                if hasattr(self.w, "id_jdl_ibadah"):
                    self.w.id_jdl_ibadah.setValue(new_id)
                msg(self, f"Data berhasil ditambahkan (ID: {new_id})")
            else:
                data.pop("id_jdl_ibadah", None)
                rows = getattr(crud, "jadwal_ibadah_update")(pk_val, data)
                msg(self, f"Perubahan disimpan ({rows} baris).")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show(self):
        self.w.show()
