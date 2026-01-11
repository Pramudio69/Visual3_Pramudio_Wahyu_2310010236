from pathlib import Path
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import QFile, Qt, QDate
from PySide6.QtUiTools import QUiLoader

from crud import CrudGereja


class FormJemaat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        UI_FILE = Path(__file__).resolve().parent / "JemaatForm.ui"
        filenya = QFile(str(UI_FILE))
        filenya.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(filenya, self)
        filenya.close()

        self.setWindowTitle("Data Jemaat")
        self.resize(self.form.size())

        self.aksi = CrudGereja()

        # setup table
        self.form.tblJemaat.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.form.tblJemaat.setSelectionMode(QAbstractItemView.SingleSelection)
        self.form.tblJemaat.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # default date
        self.form.DateTglLahir.setDate(QDate.currentDate())

        # signals
        self.form.BtnSimpan.clicked.connect(self.simpan)
        self.form.BtnUbah.clicked.connect(self.ubah)
        self.form.BtnHapus.clicked.connect(self.hapus)
        self.form.BtnBersih.clicked.connect(self.bersih)
        self.form.btnCetak.clicked.connect(self.cetak)
        self.form.lineCari.textChanged.connect(self.cari)
        self.form.tblJemaat.itemSelectionChanged.connect(self.ambil_dari_tabel)

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
        self.form.EditNama.clear()
        self.form.ComboJK.setCurrentIndex(0)
        self.form.EditAlamat.clear()
        self.form.EditTempatLahir.clear()
        self.form.DateTglLahir.setDate(QDate.currentDate())
        self.form.EditNoHP.clear()
        self.form.EditStatusKeluarga.clear()
        self.form.EditWilayah.clear()
        self.form.tblJemaat.clearSelection()
        self.form.EditNama.setFocus()
        self._set_mode_add()

    def simpan(self) -> None:
        if self.form.EditId.text().strip():
            self._info("Sedang mode edit. Gunakan tombol Ubah/Hapus, atau klik Bersih untuk tambah data baru.")
            return
        nama = self.form.EditNama.text().strip()
        jk = self.form.ComboJK.currentText().strip()
        alamat = self.form.EditAlamat.text().strip()
        tempat = self.form.EditTempatLahir.text().strip()
        tgl = self.form.DateTglLahir.date().toString("yyyy-MM-dd")
        hp = self.form.EditNoHP.text().strip()
        status = self.form.EditStatusKeluarga.text().strip()
        wilayah = self.form.EditWilayah.text().strip()

        if not nama:
            self._info("Nama jemaat belum diisi.")
            self.form.EditNama.setFocus()
            return
        if jk not in ("L", "P"):
            self._info("Jenis kelamin harus L atau P.")
            return

        try:
            self.aksi.tambah_jemaat(
                nama_jemaat=nama,
                jk_jemaat=jk,
                alamat_jemaat=alamat,
                tempat_lahir=tempat,
                tgl_lahir=tgl,
                no_hp=hp,
                status_dalam_keluarga=status,
                wilayah=wilayah,
                id_jemaat=None,
            )
        except Exception as e:
            self._info(f"Gagal simpan: {e}")
            return

        self.tampil_data()
        self.bersih()
        self._info("Data jemaat berhasil disimpan.")

    def ubah(self) -> None:
        id_text = self.form.EditId.text().strip()
        if not id_text.isdigit():
            self._info("Pilih data dari tabel terlebih dulu (ID harus ada).")
            return

        id_jemaat = int(id_text)
        nama = self.form.EditNama.text().strip()
        jk = self.form.ComboJK.currentText().strip()
        alamat = self.form.EditAlamat.text().strip()
        tempat = self.form.EditTempatLahir.text().strip()
        tgl = self.form.DateTglLahir.date().toString("yyyy-MM-dd")
        hp = self.form.EditNoHP.text().strip()
        status = self.form.EditStatusKeluarga.text().strip()
        wilayah = self.form.EditWilayah.text().strip()

        try:
            self.aksi.ubah_jemaat(id_jemaat, nama, jk, alamat, tempat, tgl, hp, status, wilayah)
        except Exception as e:
            self._info(f"Gagal ubah: {e}")
            return

        self.tampil_data()
        self._info("Data jemaat berhasil diubah.")

    def hapus(self) -> None:
        id_text = self.form.EditId.text().strip()
        if not id_text.isdigit():
            self._info("Pilih data dari tabel terlebih dulu (ID harus ada).")
            return
        if not self._confirm("Yakin menghapus data jemaat ini?"):
            return

        try:
            self.aksi.hapus_jemaat(int(id_text))
        except Exception as e:
            self._info(f"Gagal hapus: {e}")
            return

        self.tampil_data()
        self.bersih()
        self._info("Data jemaat berhasil dihapus.")

    def tampil_data(self) -> None:
        data = self.aksi.data_jemaat()
        self._isi_tabel(data)

    def cari(self) -> None:
        cari = self.form.lineCari.text().strip()
        if not cari:
            self.tampil_data()
            return
        data = self.aksi.filter_jemaat(cari)
        self._isi_tabel(data)

    def _isi_tabel(self, data) -> None:
        tbl = self.form.tblJemaat
        tbl.setRowCount(0)
        for i, r in enumerate(data):
            tbl.insertRow(i)
            tbl.setItem(i, 0, QTableWidgetItem(str(r.get("id_jemaat", ""))))
            tbl.setItem(i, 1, QTableWidgetItem(str(r.get("nama_jemaat", ""))))
            tbl.setItem(i, 2, QTableWidgetItem(str(r.get("jk_jemaat", ""))))
            tbl.setItem(i, 3, QTableWidgetItem(str(r.get("alamat_jemaat", ""))))
            tbl.setItem(i, 4, QTableWidgetItem(str(r.get("tempat_lahir", ""))))
            tbl.setItem(i, 5, QTableWidgetItem(str(r.get("tgl_lahir", ""))))
            tbl.setItem(i, 6, QTableWidgetItem(str(r.get("no_hp", ""))))
            tbl.setItem(i, 7, QTableWidgetItem(str(r.get("status_dalam_keluarga", ""))))
            tbl.setItem(i, 8, QTableWidgetItem(str(r.get("wilayah", ""))))
        tbl.resizeColumnsToContents()

    def ambil_dari_tabel(self) -> None:
        tbl = self.form.tblJemaat
        items = tbl.selectedItems()
        if not items:
            self._set_mode_add()
            return
        row = items[0].row()

        self.form.EditId.setText(tbl.item(row, 0).text())
        self.form.EditNama.setText(tbl.item(row, 1).text())
        jk = tbl.item(row, 2).text()
        self.form.ComboJK.setCurrentText(jk if jk in ("L", "P") else "L")
        self.form.EditAlamat.setText(tbl.item(row, 3).text())
        self.form.EditTempatLahir.setText(tbl.item(row, 4).text())

        # tanggal
        tgl_str = tbl.item(row, 5).text()
        qd = QDate.fromString(tgl_str, "yyyy-MM-dd")
        if qd.isValid():
            self.form.DateTglLahir.setDate(qd)

        self.form.EditNoHP.setText(tbl.item(row, 6).text())
        self.form.EditStatusKeluarga.setText(tbl.item(row, 7).text())
        self.form.EditWilayah.setText(tbl.item(row, 8).text())

        self._set_mode_edit()

        self._set_mode_edit()

    def cetak(self) -> None:
        cari = self.form.lineCari.text().strip()
        try:
            filename = self.aksi.cetak_jemaat(cari if cari else None)
            self._info(f"Berhasil membuat laporan: {filename}\n(File tersimpan di folder project)")
        except Exception as e:
            self._info(f"Gagal cetak: {e}")
