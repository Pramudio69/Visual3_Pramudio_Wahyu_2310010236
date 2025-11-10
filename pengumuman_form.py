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

class PengumumanForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = load_ui("PengumumanForm.ui")
        self.w.setParent(self)
        self.w.setWindowTitle("PengumumanForm (Sederhana)")
        self.w.btnSave.clicked.connect(self.on_save)
        self.w.btnClear.clicked.connect(self.on_clear)
        self.w.btnClose.clicked.connect(self.close)

    def _collect_data(self):
        data = {}
        data["id_pengumuman"] = self.w.id_pengumuman.value()
        data["sub_jenis"] = self.w.sub_jenis.text() if hasattr(self.w, "sub_jenis") else ""
        data["isi_pengumuman"] = self.w.isi_pengumuman.text() if hasattr(self.w, "isi_pengumuman") else ""
        return data

    def on_clear(self):
        self.w.id_pengumuman.setValue(0)
        (self.w.sub_jenis.clear() if hasattr(self.w, "sub_jenis") else None)
        (self.w.isi_pengumuman.clear() if hasattr(self.w, "isi_pengumuman") else None)
        msg(self, "Form dibersihkan.")

    def on_save(self):
        data = self._collect_data()
        pk_val = data.get("id_pengumuman", 0)
        try:
            if not pk_val:
                new_id = getattr(crud, "pengumuman_insert")(data)
                if hasattr(self.w, "id_pengumuman"):
                    self.w.id_pengumuman.setValue(new_id)
                msg(self, f"Data berhasil ditambahkan (ID: {new_id})")
            else:
                data.pop("id_pengumuman", None)
                rows = getattr(crud, "pengumuman_update")(pk_val, data)
                msg(self, f"Perubahan disimpan ({rows} baris).")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show(self):
        self.w.show()
