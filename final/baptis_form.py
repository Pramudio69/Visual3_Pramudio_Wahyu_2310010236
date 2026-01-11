# This Python file uses the following encoding: utf-8
from pathlib import Path
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader

from crud import CrudGereja


class FormBaptis(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        UI_FILE = Path(__file__).resolve().parent / "baptisForm.ui"
        filenya = QFile(str(UI_FILE))
        filenya.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(filenya, self)
        filenya.close()

        self.setWindowTitle("Data Baptis")
        self.resize(self.form.size())

        self.aksi = CrudGereja()

        self.form.tblBaptis.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.form.tblBaptis.setSelectionMode(QAbstractItemView.SingleSelection)
        self.form.tblBaptis.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.form.DateTglBaptis.setDate(QDate.currentDate())

        self.form.BtnSimpan.clicked.connect(self.simpan)
        self.form.BtnUbah.clicked.connect(self.ubah)
        self.form.BtnHapus.clicked.connect(self.hapus)
        self.form.BtnBersih.clicked.connect(self.bersih)
        self.form.btnCetak.clicked.connect(self.cetak)
        self.form.lineCari.textChanged.connect(self.cari)
        self.form.tblBaptis.itemSelectionChanged.connect(self.ambil_dari_tabel)

        # mode awal: tambah data
        self._set_mode_add()

        self.muati_combo_jemaat()
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

    def muati_combo_jemaat(self) -> None:
        self.form.ComboJemaat.clear()
        data = self.aksi.list_jemaat()
        self.form.ComboJemaat.addItem("-- Pilih Jemaat --", None)
        for r in data:
            jid = r["id_jemaat"]
            nm = r.get("nama_jemaat") or ""
            self.form.ComboJemaat.addItem(f"{jid} - {nm}", jid)

    def bersih(self) -> None:
        self.form.EditId.clear()
        self.form.ComboJemaat.setCurrentIndex(0)
        self.form.EditAyah.clear()
        self.form.EditIbu.clear()
        self.form.EditWali.clear()
        self.form.DateTglBaptis.setDate(QDate.currentDate())
        self.form.EditPelayan.clear()
        self.form.EditSurat.clear()
        self.form.tblBaptis.clearSelection()
        self.form.ComboJemaat.setFocus()
        self._set_mode_add()
        self._set_mode_add()

    def simpan(self) -> None:
        if self.form.EditId.text().strip():
            self._info("Sedang mode edit. Gunakan tombol Ubah/Hapus, atau klik Bersih untuk tambah data baru.")
            return
        id_combo = self.form.ComboJemaat.currentData()
        if not id_combo:
            self._info("Silakan pilih Jemaat terlebih dahulu.")
            return

        id_baptis = None

        ayah = self.form.EditAyah.text().strip()
        ibu = self.form.EditIbu.text().strip()
        wali = self.form.EditWali.text().strip()
        tgl = self.form.DateTglBaptis.date().toString("yyyy-MM-dd")
        pelayan = self.form.EditPelayan.text().strip()
        surat = self.form.EditSurat.text().strip()

        try:
            self.aksi.tambah_baptis(
                id_jemaat=int(id_combo),
                nama_ayah=ayah,
                nama_ibu=ibu,
                nama_wali=wali,
                tgl_baptis=tgl,
                pelayan=pelayan,
                surat_baptis=surat,
                id_baptis=id_baptis,
            )
        except Exception as e:
            self._info(f"Gagal simpan: {e}")
            return

        self.tampil_data()
        self.bersih()
        self._info("Data baptis berhasil disimpan.")

    def ubah(self) -> None:
        id_text = self.form.EditId.text().strip()
        if not id_text.isdigit():
            self._info("Pilih data dari tabel terlebih dulu (ID harus ada).")
            return

        id_combo = self.form.ComboJemaat.currentData()
        if not id_combo:
            self._info("Silakan pilih Jemaat terlebih dahulu.")
            return

        ayah = self.form.EditAyah.text().strip()
        ibu = self.form.EditIbu.text().strip()
        wali = self.form.EditWali.text().strip()
        tgl = self.form.DateTglBaptis.date().toString("yyyy-MM-dd")
        pelayan = self.form.EditPelayan.text().strip()
        surat = self.form.EditSurat.text().strip()

        try:
            self.aksi.ubah_baptis(int(id_text), int(id_combo), ayah, ibu, wali, tgl, pelayan, surat)
        except Exception as e:
            self._info(f"Gagal ubah: {e}")
            return

        self.tampil_data()
        self._info("Data baptis berhasil diubah.")

    def hapus(self) -> None:
        id_text = self.form.EditId.text().strip()
        if not id_text.isdigit():
            self._info("Pilih data dari tabel terlebih dulu (ID harus ada).")
            return
        if not self._confirm("Yakin menghapus data baptis ini?"):
            return

        try:
            self.aksi.hapus_baptis(int(id_text))
        except Exception as e:
            self._info(f"Gagal hapus: {e}")
            return

        self.tampil_data()
        self.bersih()
        self._info("Data baptis berhasil dihapus.")

    def tampil_data(self) -> None:
        data = self.aksi.data_baptis()
        self._isi_tabel(data)

    def cari(self) -> None:
        cari = self.form.lineCari.text().strip()
        if not cari:
            self.tampil_data()
            return
        data = self.aksi.filter_baptis(cari)
        self._isi_tabel(data)

    def _isi_tabel(self, data) -> None:
        tbl = self.form.tblBaptis
        tbl.setRowCount(0)
        for i, r in enumerate(data):
            tbl.insertRow(i)
            tbl.setItem(i, 0, QTableWidgetItem(str(r.get("id_baptis", ""))))
            tbl.setItem(i, 1, QTableWidgetItem(str(r.get("id_jemaat", ""))))
            tbl.setItem(i, 2, QTableWidgetItem(str(r.get("nama_jemaat", ""))))
            tbl.setItem(i, 3, QTableWidgetItem(str(r.get("nama_ayah", ""))))
            tbl.setItem(i, 4, QTableWidgetItem(str(r.get("nama_ibu", ""))))
            tbl.setItem(i, 5, QTableWidgetItem(str(r.get("nama_wali", ""))))
            tbl.setItem(i, 6, QTableWidgetItem(str(r.get("tgl_baptis", ""))))
            tbl.setItem(i, 7, QTableWidgetItem(str(r.get("pelayan", ""))))
            tbl.setItem(i, 8, QTableWidgetItem(str(r.get("surat_baptis", ""))))
        tbl.resizeColumnsToContents()

    def ambil_dari_tabel(self) -> None:
        tbl = self.form.tblBaptis
        items = tbl.selectedItems()
        if not items:
            self._set_mode_add()
            return
        row = items[0].row()

        self.form.EditId.setText(tbl.item(row, 0).text())

        id_jemaat = tbl.item(row, 1).text()
        for i in range(self.form.ComboJemaat.count()):
            if str(self.form.ComboJemaat.itemData(i)) == id_jemaat:
                self.form.ComboJemaat.setCurrentIndex(i)
                break

        self.form.EditAyah.setText(tbl.item(row, 3).text())
        self.form.EditIbu.setText(tbl.item(row, 4).text())
        self.form.EditWali.setText(tbl.item(row, 5).text())

        tgl_str = tbl.item(row, 6).text()
        qd = QDate.fromString(tgl_str, "yyyy-MM-dd")
        if qd.isValid():
            self.form.DateTglBaptis.setDate(qd)

        self.form.EditPelayan.setText(tbl.item(row, 7).text())
        self.form.EditSurat.setText(tbl.item(row, 8).text())

        self._set_mode_edit()

    def cetak(self) -> None:
        cari = self.form.lineCari.text().strip()
        try:
            filename = self.aksi.cetak_baptis(cari if cari else None)
            self._info(f"Berhasil membuat laporan: {filename}\n(File tersimpan di folder project)")
        except Exception as e:
            self._info(f"Gagal cetak: {e}")
