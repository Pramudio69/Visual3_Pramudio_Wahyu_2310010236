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

class AdminForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = load_ui("AdminForm.ui")
        self.w.setParent(self)
        self.w.setWindowTitle("AdminForm (Sederhana)")
        self.w.btnSave.clicked.connect(self.on_save)
        self.w.btnClear.clicked.connect(self.on_clear)
        self.w.btnClose.clicked.connect(self.close)

    def _collect_data(self):
        data = {}
        data["id_admin"] = self.w.id_admin.value()
        data["username"] = self.w.username.text() if hasattr(self.w, "username") else ""
        data["password"] = self.w.password.text() if hasattr(self.w, "password") else ""
        data["nama_admin"] = self.w.nama_admin.text() if hasattr(self.w, "nama_admin") else ""
        data["level"] = self.w.level.currentText() if hasattr(self.w, "level") else None
        return data

    def on_clear(self):
        self.w.id_admin.setValue(0)
        (self.w.username.clear() if hasattr(self.w, "username") else None)
        (self.w.password.clear() if hasattr(self.w, "password") else None)
        (self.w.nama_admin.clear() if hasattr(self.w, "nama_admin") else None)
        (self.w.level.setCurrentIndex(0) if hasattr(self.w, "level") else None)
        msg(self, "Form dibersihkan.")

    def on_save(self):
        data = self._collect_data()
        pk_val = data.get("id_admin", 0)
        try:
            if not pk_val:
                new_id = getattr(crud, "admin_insert")(data)
                if hasattr(self.w, "id_admin"):
                    self.w.id_admin.setValue(new_id)
                msg(self, f"Data berhasil ditambahkan (ID: {new_id})")
            else:
                data.pop("id_admin", None)
                rows = getattr(crud, "admin_update")(pk_val, data)
                msg(self, f"Perubahan disimpan ({rows} baris).")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show(self):
        self.w.show()
