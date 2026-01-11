from pathlib import Path
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud import CrudGereja


class FormPengumuman(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        UI_FILE = Path(__file__).resolve().parent / "PengumumanForm.ui"
        filenya = QFile(str(UI_FILE))
        filenya.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(filenya, self)
        filenya.close()

        self.setWindowTitle("Data Pengumuman")
        self.resize(self.form.size())

        self.aksi = CrudGereja()

        self.form.tblPengumuman.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.form.tblPengumuman.setSelectionMode(QAbstractItemView.SingleSelection)
        self.form.tblPengumuman.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.form.BtnSimpan.clicked.connect(self.simpan)
        self.form.BtnUbah.clicked.connect(self.ubah)
        self.form.BtnHapus.clicked.connect(self.hapus)
        self.form.BtnBersih.clicked.connect(self.bersih)
        self.form.btnCetak.clicked.connect(self.cetak)
        self.form.lineCari.textChanged.connect(self.cari)
        self.form.tblPengumuman.itemSelectionChanged.connect(self.ambil_dari_tabel)

        self._set_mode_add()

        self.tampil_data()

    def _set_mode_add(self) -> None:
        self.form.BtnSimpan.setEnabled(True)
        self.form.BtnUbah.setEnabled(False)
        self.form.BtnHapus.setEnabled(False)
        try:
            self.form.EditId.setReadOnly(True)
        except Exception:
            pass

    def _set_mode_edit(self) -> None:
        self.form.BtnSimpan.setEnabled(False)
        self.form.BtnUbah.setEnabled(True)
        self.form.BtnHapus.setEnabled(True)

    def _info(self, msg: str) -> None:
        QMessageBox.information(self, "Informasi", msg)

    def _confirm(self, msg: str) -> bool:
        res = QMessageBox.question(self, "Konfirmasi", msg, QMessageBox.Yes | QMessageBox.No)
        return res == QMessageBox.Yes

    def bersih(self) -> None:
        self.form.EditId.clear()
        self.form.EditSub.clear()
        self.form.EditIsi.clear()
        self.form.tblPengumuman.clearSelection()
        self.form.EditSub.setFocus()
        self._set_mode_add()

    def simpan(self) -> None:
        if self.form.EditId.text().strip():
            self._info("Sedang mode edit. Gunakan tombol Ubah/Hapus, atau klik Bersih untuk tambah data baru.")
            return
        sub = self.form.EditSub.text().strip()
        isi = self.form.EditIsi.text().strip()
        if not sub:
            self._info("Sub jenis belum diisi.")
            return
        if not isi:
            self._info("Isi pengumuman belum diisi.")
            return

        try:
            self.aksi.tambah_pengumuman(sub, isi, id_pengumuman=None)
        except Exception as e:
            self._info(f"Gagal simpan: {e}")
            return

        self.tampil_data()
        self.bersih()
        self._info("Pengumuman berhasil disimpan.")

    def ubah(self) -> None:
        id_text = self.form.EditId.text().strip()
        if not id_text.isdigit():
            self._info("Pilih data dari tabel terlebih dulu (ID harus ada).")
            return

        sub = self.form.EditSub.text().strip()
        isi = self.form.EditIsi.text().strip()

        try:
            self.aksi.ubah_pengumuman(int(id_text), sub, isi)
        except Exception as e:
            self._info(f"Gagal ubah: {e}")
            return

        self.tampil_data()
        self._info("Pengumuman berhasil diubah.")

    def hapus(self) -> None:
        id_text = self.form.EditId.text().strip()
        if not id_text.isdigit():
            self._info("Pilih data dari tabel terlebih dulu (ID harus ada).")
            return
        if not self._confirm("Yakin menghapus pengumuman ini?"):
            return

        try:
            self.aksi.hapus_pengumuman(int(id_text))
        except Exception as e:
            self._info(f"Gagal hapus: {e}")
            return

        self.tampil_data()
        self.bersih()
        self._info("Pengumuman berhasil dihapus.")

    def tampil_data(self) -> None:
        data = self.aksi.data_pengumuman()
        self._isi_tabel(data)

    def cari(self) -> None:
        cari = self.form.lineCari.text().strip()
        if not cari:
            self.tampil_data()
            return
        data = self.aksi.filter_pengumuman(cari)
        self._isi_tabel(data)

    def _isi_tabel(self, data) -> None:
        tbl = self.form.tblPengumuman
        tbl.setRowCount(0)
        for i, r in enumerate(data):
            tbl.insertRow(i)
            tbl.setItem(i, 0, QTableWidgetItem(str(r.get("id_pengumuman", ""))))
            tbl.setItem(i, 1, QTableWidgetItem(str(r.get("sub_jenis", ""))))
            tbl.setItem(i, 2, QTableWidgetItem(str(r.get("isi_pengumuman", ""))))
        tbl.resizeColumnsToContents()

    def ambil_dari_tabel(self) -> None:
        tbl = self.form.tblPengumuman
        items = tbl.selectedItems()
        if not items:
            self._set_mode_add()
            return
        row = items[0].row()

        self.form.EditId.setText(tbl.item(row, 0).text())
        self.form.EditSub.setText(tbl.item(row, 1).text())
        self.form.EditIsi.setText(tbl.item(row, 2).text())

        self._set_mode_edit()

        self._set_mode_edit()

    def cetak(self) -> None:
        cari = self.form.lineCari.text().strip()
        try:
            filename = self.aksi.cetak_pengumuman(cari if cari else None)
            self._info(f"Berhasil membuat laporan: {filename}\n(File tersimpan di folder project)")
        except Exception as e:
            self._info(f"Gagal cetak: {e}")
