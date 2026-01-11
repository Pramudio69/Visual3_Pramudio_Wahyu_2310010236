import mysql.connector

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from typing import Optional, List, Dict, Any

class CrudGereja:
    def __init__(
        self,
        host: str = "localhost",
        user: str = "root",
        password: str = "",
        database: str = "db_2310010236",
    ) -> None:
        self.koneksi = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            autocommit=True,
        )

    def _fetchall_dict(self, query, params=None):
        cur = self.koneksi.cursor(dictionary=True)
        cur.execute(query, params or ())
        rows = cur.fetchall()
        cur.close()
        return rows

    def _execute(self, query, params=None):
        cur = self.koneksi.cursor()
        cur.execute(query, params or ())
        try:
            self.koneksi.commit()
        except Exception:
            pass
        last_id = cur.lastrowid or 0
        self.last_rowcount = cur.rowcount
        cur.close()
        return last_id

    def _cetak_pdf(self, filename, header, rows, col_widths=None):
        data = [header] + [list(r) for r in rows]
        pdf = SimpleDocTemplate(filename, pagesize=landscape(A4))
        table = Table(data, colWidths=col_widths)
        style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
            ]
        )
        table.setStyle(style)
        pdf.build([table])

    def tambah_jemaat(
        self,
        nama_jemaat: str,
        jk_jemaat: str,
        alamat_jemaat: str,
        tempat_lahir: str,
        tgl_lahir: str,
        no_hp: str,
        status_dalam_keluarga: str,
        wilayah: str,
        id_jemaat = None,
    ) -> int:
        if id_jemaat:
            last_id, _ = self._execute(
                """
                INSERT INTO jemaat
                (id_jemaat, nama_jemaat, jk_jemaat, alamat_jemaat, tempat_lahir, tgl_lahir, no_hp, status_dalam_keluarga, wilayah)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (id_jemaat, nama_jemaat, jk_jemaat, alamat_jemaat, tempat_lahir, tgl_lahir, no_hp, status_dalam_keluarga, wilayah),
            )
            return last_id
        last_id, _ = self._execute(
            """
            INSERT INTO jemaat
            (nama_jemaat, jk_jemaat, alamat_jemaat, tempat_lahir, tgl_lahir, no_hp, status_dalam_keluarga, wilayah)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (nama_jemaat, jk_jemaat, alamat_jemaat, tempat_lahir, tgl_lahir, no_hp, status_dalam_keluarga, wilayah),
        )
        return last_id

    def ubah_jemaat(
        self,
        id_jemaat: int,
        nama_jemaat: str,
        jk_jemaat: str,
        alamat_jemaat: str,
        tempat_lahir: str,
        tgl_lahir: str,
        no_hp: str,
        status_dalam_keluarga: str,
        wilayah: str,
    ) -> None:
        self._execute(
            """
            UPDATE jemaat
            SET nama_jemaat=%s, jk_jemaat=%s, alamat_jemaat=%s, tempat_lahir=%s, tgl_lahir=%s,
                no_hp=%s, status_dalam_keluarga=%s, wilayah=%s
            WHERE id_jemaat=%s
            """,
            (nama_jemaat, jk_jemaat, alamat_jemaat, tempat_lahir, tgl_lahir, no_hp, status_dalam_keluarga, wilayah, id_jemaat),
        )

    def hapus_jemaat(self, id_jemaat: int) -> None:
        self._execute("DELETE FROM baptis WHERE id_jemaat=%s", (id_jemaat,))
        self._execute("DELETE FROM jadwal_ibadah WHERE id_jemaat=%s", (id_jemaat,))
        self._execute("DELETE FROM jemaat WHERE id_jemaat=%s", (id_jemaat,))

    def data_jemaat(self):
        return self._fetchall_dict("SELECT * FROM jemaat ORDER BY id_jemaat ASC")

    def filter_jemaat(self, cari: str):
        like = f"%{cari}%"
        return self._fetchall_dict(
            """
            SELECT * FROM jemaat
            WHERE CAST(id_jemaat AS CHAR) LIKE %s
               OR nama_jemaat LIKE %s
               OR jk_jemaat LIKE %s
               OR alamat_jemaat LIKE %s
               OR tempat_lahir LIKE %s
               OR CAST(tgl_lahir AS CHAR) LIKE %s
               OR no_hp LIKE %s
               OR status_dalam_keluarga LIKE %s
               OR wilayah LIKE %s
            ORDER BY id_jemaat ASC
            """,
            (like, like, like, like, like, like, like, like, like),
        )

    def list_jemaat(self):
        return self._fetchall_dict("SELECT id_jemaat, nama_jemaat FROM jemaat ORDER BY id_jemaat ASC")

    def cetak_jemaat(self, cari = None):
        if cari and cari.strip():
            rows = self._fetchall_dict(
                """
                SELECT id_jemaat, nama_jemaat, jk_jemaat, alamat_jemaat, tempat_lahir, tgl_lahir, no_hp, status_dalam_keluarga, wilayah
                FROM jemaat
                WHERE CAST(id_jemaat AS CHAR) LIKE %s OR nama_jemaat LIKE %s OR wilayah LIKE %s
                ORDER BY id_jemaat ASC
                """,
                (f"%{cari}%", f"%{cari}%", f"%{cari}%"),
            )
            filename = "Laporan_Jemaat_Filter.pdf"
        else:
            rows = self._fetchall_dict(
                """
                SELECT id_jemaat, nama_jemaat, jk_jemaat, alamat_jemaat, tempat_lahir, tgl_lahir, no_hp, status_dalam_keluarga, wilayah
                FROM jemaat
                ORDER BY id_jemaat ASC
                """
            )
            filename = "Laporan_Jemaat.pdf"

        header = ["ID", "Nama", "JK", "Alamat", "Tempat Lahir", "Tgl Lahir", "No HP", "Status Keluarga", "Wilayah"]
        data_rows = [[r["id_jemaat"], r["nama_jemaat"], r["jk_jemaat"], r["alamat_jemaat"], r["tempat_lahir"], str(r["tgl_lahir"]), r["no_hp"], r["status_dalam_keluarga"], r["wilayah"]] for r in rows]
        self._cetak_pdf(filename, header, data_rows, col_widths=[40, 110, 25, 150, 80, 65, 70, 90, 70])
        return filename

    def tambah_baptis(
        self,
        id_jemaat: int,
        nama_ayah: str,
        nama_ibu: str,
        nama_wali: str,
        tgl_baptis: str,
        pelayan: str,
        surat_baptis: str,
        id_baptis: Optional[int] = None,
    ) -> int:
        if id_baptis:
            return self._execute(
                """
                INSERT INTO baptis
                (id_baptis, id_jemaat, nama_ayah, nama_ibu, nama_wali, tgl_baptis, pelayan, surat_baptis)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (id_baptis, id_jemaat, nama_ayah, nama_ibu, nama_wali, tgl_baptis, pelayan, surat_baptis),
            )
        return self._execute(
            """
            INSERT INTO baptis
            (id_jemaat, nama_ayah, nama_ibu, nama_wali, tgl_baptis, pelayan, surat_baptis)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            """,
            (id_jemaat, nama_ayah, nama_ibu, nama_wali, tgl_baptis, pelayan, surat_baptis),
        )

    def ubah_baptis(
        self,
        id_baptis: int,
        id_jemaat: int,
        nama_ayah: str,
        nama_ibu: str,
        nama_wali: str,
        tgl_baptis: str,
        pelayan: str,
        surat_baptis: str,
    ) -> None:
        self._execute(
            """
            UPDATE baptis
            SET id_jemaat=%s, nama_ayah=%s, nama_ibu=%s, nama_wali=%s, tgl_baptis=%s, pelayan=%s, surat_baptis=%s
            WHERE id_baptis=%s
            """,
            (id_jemaat, nama_ayah, nama_ibu, nama_wali, tgl_baptis, pelayan, surat_baptis, id_baptis),
        )

    def hapus_baptis(self, id_baptis: int) -> None:
        self._execute("DELETE FROM baptis WHERE id_baptis=%s", (id_baptis,))

    def data_baptis(self):
        return self._fetchall_dict(
            """
            SELECT b.*, j.nama_jemaat
            FROM baptis b
            LEFT JOIN jemaat j ON j.id_jemaat=b.id_jemaat
            ORDER BY b.id_baptis ASC
            """
        )

    def filter_baptis(self, cari: str) -> List[Dict[str, Any]]:
        like = f"%{cari}%"
        return self._fetchall_dict(
            """
            SELECT b.*, j.nama_jemaat
            FROM baptis b
            LEFT JOIN jemaat j ON j.id_jemaat=b.id_jemaat
            WHERE CAST(b.id_baptis AS CHAR) LIKE %s
               OR CAST(b.id_jemaat AS CHAR) LIKE %s
               OR j.nama_jemaat LIKE %s
               OR b.nama_ayah LIKE %s
               OR b.nama_ibu LIKE %s
               OR b.nama_wali LIKE %s
               OR CAST(b.tgl_baptis AS CHAR) LIKE %s
               OR b.pelayan LIKE %s
               OR b.surat_baptis LIKE %s
            ORDER BY b.id_baptis ASC
            """,
            (like, like, like, like, like, like, like, like, like),
        )

    def cetak_baptis(self, cari: Optional[str] = None) -> str:
        if cari and cari.strip():
            rows = self.filter_baptis(cari)
            filename = "Laporan_Baptis_Filter.pdf"
        else:
            rows = self.data_baptis()
            filename = "Laporan_Baptis.pdf"
        header = ["ID", "ID Jemaat", "Nama Jemaat", "Ayah", "Ibu", "Wali", "Tgl Baptis", "Pelayan", "Surat"]
        data_rows = [
            [
                r["id_baptis"],
                r["id_jemaat"],
                r.get("nama_jemaat") or "",
                r.get("nama_ayah") or "",
                r.get("nama_ibu") or "",
                r.get("nama_wali") or "",
                str(r.get("tgl_baptis") or ""),
                r.get("pelayan") or "",
                r.get("surat_baptis") or "",
            ]
            for r in rows
        ]
        self._cetak_pdf(filename, header, data_rows, col_widths=[40, 55, 110, 80, 80, 80, 70, 90, 110])
        return filename

    def tambah_jadwal_ibadah(
        self,
        id_jemaat: int,
        tgl_ibadah: str,
        wilayah: str,
        hari_ibadah: str,
        jam_ibadah: str,
        pemimpin_ibadah: str,
        id_jdl_ibadah: Optional[int] = None,
    ) -> int:
        if id_jdl_ibadah:
            return self._execute(
                """
                INSERT INTO jadwal_ibadah
                (id_jdl_ibadah, id_jemaat, tgl_ibadah, wilayah, hari_ibadah, jam_ibadah, pemimpin_ibadah)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
                """,
                (id_jdl_ibadah, id_jemaat, tgl_ibadah, wilayah, hari_ibadah, jam_ibadah, pemimpin_ibadah),
            )
        return self._execute(
            """
            INSERT INTO jadwal_ibadah
            (id_jemaat, tgl_ibadah, wilayah, hari_ibadah, jam_ibadah, pemimpin_ibadah)
            VALUES (%s,%s,%s,%s,%s,%s)
            """,
            (id_jemaat, tgl_ibadah, wilayah, hari_ibadah, jam_ibadah, pemimpin_ibadah),
        )

    def ubah_jadwal_ibadah(
        self,
        id_jdl_ibadah: int,
        id_jemaat: int,
        tgl_ibadah: str,
        wilayah: str,
        hari_ibadah: str,
        jam_ibadah: str,
        pemimpin_ibadah: str,
    ) -> None:
        self._execute(
            """
            UPDATE jadwal_ibadah
            SET id_jemaat=%s, tgl_ibadah=%s, wilayah=%s, hari_ibadah=%s, jam_ibadah=%s, pemimpin_ibadah=%s
            WHERE id_jdl_ibadah=%s
            """,
            (id_jemaat, tgl_ibadah, wilayah, hari_ibadah, jam_ibadah, pemimpin_ibadah, id_jdl_ibadah),
        )

    def hapus_jadwal_ibadah(self, id_jdl_ibadah: int) -> None:
        self._execute("DELETE FROM jadwal_ibadah WHERE id_jdl_ibadah=%s", (id_jdl_ibadah,))

    def data_jadwal_ibadah(self) -> List[Dict[str, Any]]:
        return self._fetchall_dict(
            """
            SELECT ji.*, j.nama_jemaat
            FROM jadwal_ibadah ji
            LEFT JOIN jemaat j ON j.id_jemaat=ji.id_jemaat
            ORDER BY ji.id_jdl_ibadah ASC
            """
        )

    def filter_jadwal_ibadah(self, cari: str) -> List[Dict[str, Any]]:
        like = f"%{cari}%"
        return self._fetchall_dict(
            """
            SELECT ji.*, j.nama_jemaat
            FROM jadwal_ibadah ji
            LEFT JOIN jemaat j ON j.id_jemaat=ji.id_jemaat
            WHERE CAST(ji.id_jdl_ibadah AS CHAR) LIKE %s
               OR CAST(ji.id_jemaat AS CHAR) LIKE %s
               OR j.nama_jemaat LIKE %s
               OR CAST(ji.tgl_ibadah AS CHAR) LIKE %s
               OR ji.wilayah LIKE %s
               OR ji.hari_ibadah LIKE %s
               OR ji.jam_ibadah LIKE %s
               OR ji.pemimpin_ibadah LIKE %s
            ORDER BY ji.id_jdl_ibadah ASC
            """,
            (like, like, like, like, like, like, like, like),
        )

    def cetak_jadwal_ibadah(self, cari: Optional[str] = None) -> str:
        if cari and cari.strip():
            rows = self.filter_jadwal_ibadah(cari)
            filename = "Laporan_Jadwal_Ibadah_Filter.pdf"
        else:
            rows = self.data_jadwal_ibadah()
            filename = "Laporan_Jadwal_Ibadah.pdf"

        header = ["ID", "ID Jemaat", "Nama Jemaat", "Tgl Ibadah", "Wilayah", "Hari", "Jam", "Pemimpin"]
        data_rows = [
            [
                r["id_jdl_ibadah"],
                r["id_jemaat"],
                r.get("nama_jemaat") or "",
                str(r.get("tgl_ibadah") or ""),
                r.get("wilayah") or "",
                r.get("hari_ibadah") or "",
                r.get("jam_ibadah") or "",
                r.get("pemimpin_ibadah") or "",
            ]
            for r in rows
        ]
        self._cetak_pdf(filename, header, data_rows, col_widths=[40, 55, 110, 70, 70, 70, 60, 110])
        return filename

    def tambah_pengumuman(self, sub_jenis: str, isi_pengumuman: str, id_pengumuman: Optional[int] = None) -> int:
        if id_pengumuman:
            return self._execute(
                "INSERT INTO pengumuman (id_pengumuman, sub_jenis, isi_pengumuman) VALUES (%s,%s,%s)",
                (id_pengumuman, sub_jenis, isi_pengumuman),
            )
        return self._execute(
            "INSERT INTO pengumuman (sub_jenis, isi_pengumuman) VALUES (%s,%s)",
            (sub_jenis, isi_pengumuman),
        )

    def ubah_pengumuman(self, id_pengumuman: int, sub_jenis: str, isi_pengumuman: str) -> None:
        self._execute(
            "UPDATE pengumuman SET sub_jenis=%s, isi_pengumuman=%s WHERE id_pengumuman=%s",
            (sub_jenis, isi_pengumuman, id_pengumuman),
        )

    def hapus_pengumuman(self, id_pengumuman: int) -> None:
        self._execute("DELETE FROM pengumuman WHERE id_pengumuman=%s", (id_pengumuman,))

    def data_pengumuman(self) -> List[Dict[str, Any]]:
        return self._fetchall_dict("SELECT * FROM pengumuman ORDER BY id_pengumuman ASC")

    def filter_pengumuman(self, cari: str) -> List[Dict[str, Any]]:
        like = f"%{cari}%"
        return self._fetchall_dict(
            """
            SELECT * FROM pengumuman
            WHERE CAST(id_pengumuman AS CHAR) LIKE %s
               OR sub_jenis LIKE %s
               OR isi_pengumuman LIKE %s
            ORDER BY id_pengumuman ASC
            """,
            (like, like, like),
        )

    def cetak_pengumuman(self, cari: Optional[str] = None) -> str:
        if cari and cari.strip():
            rows = self.filter_pengumuman(cari)
            filename = "Laporan_Pengumuman_Filter.pdf"
        else:
            rows = self.data_pengumuman()
            filename = "Laporan_Pengumuman.pdf"
        header = ["ID", "Sub Jenis", "Isi Pengumuman"]
        data_rows = [[r["id_pengumuman"], r.get("sub_jenis") or "", r.get("isi_pengumuman") or ""] for r in rows]
        self._cetak_pdf(filename, header, data_rows, col_widths=[40, 120, 420])
        return filename

    def tambah_admin(
        self,
        username: str,
        password_hash: str,
        nama_admin: str,
        level: str,
        id_admin: Optional[int] = None,
    ) -> int:
        if id_admin:
            return self._execute(
                "INSERT INTO admin (id_admin, username, password, nama_admin, level) VALUES (%s,%s,%s,%s,%s)",
                (id_admin, username, password_hash, nama_admin, level),
            )
        return self._execute(
            "INSERT INTO admin (username, password, nama_admin, level) VALUES (%s,%s,%s,%s)",
            (username, password_hash, nama_admin, level),
        )

    def ubah_admin(self, id_admin: int, username: str, password_hash: str, nama_admin: str, level: str) -> None:
        self._execute(
            "UPDATE admin SET username=%s, password=%s, nama_admin=%s, level=%s WHERE id_admin=%s",
            (username, password_hash, nama_admin, level, id_admin),
        )

    def hapus_admin(self, id_admin: int) -> None:
        self._execute("DELETE FROM admin WHERE id_admin=%s", (id_admin,))

    def data_admin(self) -> List[Dict[str, Any]]:
        return self._fetchall_dict("SELECT id_admin, username, nama_admin, level FROM admin ORDER BY id_admin ASC")

    def filter_admin(self, cari: str) -> List[Dict[str, Any]]:
        like = f"%{cari}%"
        return self._fetchall_dict(
            """
            SELECT id_admin, username, nama_admin, level
            FROM admin
            WHERE CAST(id_admin AS CHAR) LIKE %s
               OR username LIKE %s
               OR nama_admin LIKE %s
               OR level LIKE %s
            ORDER BY id_admin ASC
            """,
            (like, like, like, like),
        )
