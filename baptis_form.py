# baptis_form.py — Id Jemaat pakai ComboBox (lookup dari tabel jemaat)
from PySide6.QtWidgets import QWidget, QMessageBox, QComboBox
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader
import crud

def load_ui(path):
    f = QFile(path); f.open(QFile.ReadOnly)
    w = QUiLoader().load(f); f.close()
    return w

def msg(parent, text):
    QMessageBox.information(parent, 'Info', text)

class BaptisForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = load_ui('BaptisForm.ui')
        self.w.setParent(self)
        self.w.setWindowTitle('BaptisForm (Sederhana)')

        self._setup_id_jemaat_combobox()

        self.w.btnSave.clicked.connect(self.on_save)
        self.w.btnClear.clicked.connect(self.on_clear)
        self.w.btnClose.clicked.connect(self.close)

    def _setup_id_jemaat_combobox(self):
        self._id_as_combo = False
        w = getattr(self.w, 'id_jemaat', None)
        if isinstance(w, QComboBox):
            self._id_as_combo = True
            w.clear()
            try:
                rows = crud.jemaat_list()
                if not rows:
                    QMessageBox.warning(self, 'Peringatan', 'Tabel jemaat masih kosong. Tambah jemaat dulu.')
                for r in rows:
                    label = f"{r['id_jemaat']} - {r.get('nama_jemaat','')}"
                    w.addItem(label, r['id_jemaat'])
            except Exception as e:
                QMessageBox.warning(self, 'Peringatan', f'Gagal memuat daftar jemaat: {e}')

    def _collect_data(self):
        data = {}
        data['id_baptis'] = self.w.id_baptis.value() if hasattr(self.w, 'id_baptis') else 0
        if self._id_as_combo:
            data['id_jemaat'] = self.w.id_jemaat.currentData()
        else:
            data['id_jemaat'] = self.w.id_jemaat.value() if hasattr(self.w, 'id_jemaat') else None
        data['nama_ayah']    = self.w.nama_ayah.text()    if hasattr(self.w, 'nama_ayah') else ''
        data['nama_ibu']     = self.w.nama_ibu.text()     if hasattr(self.w, 'nama_ibu') else ''
        data['nama_wali']    = self.w.nama_wali.text()    if hasattr(self.w, 'nama_wali') else ''
        data['tgl_baptis']   = self.w.tgl_baptis.date().toString('yyyy-MM-dd') if hasattr(self.w, 'tgl_baptis') else None
        data['pelayan']      = self.w.pelayan.text()      if hasattr(self.w, 'pelayan') else ''
        data['surat_baptis'] = self.w.surat_baptis.text() if hasattr(self.w, 'surat_baptis') else ''
        return data

    def on_clear(self):
        if hasattr(self.w, 'id_baptis'): self.w.id_baptis.setValue(0)
        if self._id_as_combo:
            self.w.id_jemaat.setCurrentIndex(0)
        elif hasattr(self.w, 'id_jemaat'):
            self.w.id_jemaat.setValue(0)
        for name in ['nama_ayah','nama_ibu','nama_wali','pelayan','surat_baptis']:
            if hasattr(self.w, name): getattr(self.w, name).clear()
        if hasattr(self.w, 'tgl_baptis'): self.w.tgl_baptis.setDate(QDate.currentDate())
        msg(self, 'Form dibersihkan.')

    def on_save(self):
        data = self._collect_data()
        pk_val = data.get('id_baptis', 0)
        try:
            if not data.get('id_jemaat'):
                raise ValueError('Pilih Jemaat terlebih dahulu.')
            if not pk_val:
                new_id = crud.baptis_insert(data)
                if hasattr(self.w, 'id_baptis'): self.w.id_baptis.setValue(new_id)
                msg(self, f'Data berhasil ditambahkan (ID: {new_id})')
            else:
                data.pop('id_baptis', None)
                rows = crud.baptis_update(pk_val, data)
                msg(self, f'Perubahan disimpan ({rows} baris).')
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def show(self):
        self.w.show()
