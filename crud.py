# crud.py (mysql.connector, class-based + wrapper, lazy connect) — no 'admin' table
from typing import Dict, Any
import mysql.connector
from mysql.connector import errors

class crud:
    def __init__(self):
        try:
            self.koneksi = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_2310010236',
                autocommit=True
            )
        except errors.ProgrammingError as e:
            if e.errno == 1049:
                raise RuntimeError("Database 'db_2310010236' belum ada. Buat dulu atau ganti nama DB di crud.py.") from e
            raise

    def _cursor(self, dict_cursor: bool = False):
        if not self.koneksi.is_connected():
            self.koneksi.reconnect(attempts=2, delay=1)
        return self.koneksi.cursor(dictionary=dict_cursor)

    def insert(self, table: str, data: Dict[str, Any]) -> int:
        if not data: raise ValueError("Data kosong untuk INSERT.")
        keys = ", ".join(f"`{k}`" for k in data.keys())
        vals = ", ".join(["%s"] * len(data))
        sql = f"INSERT INTO `{table}` ({keys}) VALUES ({vals})"
        cur = self._cursor()
        try:
            cur.execute(sql, list(data.values()))
            return int(cur.lastrowid or 0)
        finally:
            cur.close()

    def update(self, table: str, pk_col: str, pk_val, data: Dict[str, Any]) -> int:
        if not data: return 0
        sets = ", ".join(f"`{k}`=%s" for k in data.keys())
        sql = f"UPDATE `{table}` SET {sets} WHERE `{pk_col}`=%s"
        cur = self._cursor()
        try:
            cur.execute(sql, [*data.values(), pk_val])
            return int(cur.rowcount)
        finally:
            cur.close()

    def delete(self, table: str, pk_col: str, pk_val) -> int:
        sql = f"DELETE FROM `{table}` WHERE `{pk_col}`=%s"
        cur = self._cursor()
        try:
            cur.execute(sql, (pk_val,))
            return int(cur.rowcount)
        finally:
            cur.close()

    def get_by_id(self, table: str, pk_col: str, pk_val):
        sql = f"SELECT * FROM `{table}` WHERE `{pk_col}`=%s"
        cur = self._cursor(dict_cursor=True)
        try:
            cur.execute(sql, (pk_val,))
            return cur.fetchone()
        finally:
            cur.close()

    def list_all(self, table: str, order_by: str):
        sql = f"SELECT * FROM `{table}` ORDER BY `{order_by}` ASC"
        cur = self._cursor(dict_cursor=True)
        try:
            cur.execute(sql)
            return cur.fetchall()
        finally:
            cur.close()

    # ---- table wrappers (no admin) ----
    # BAPTIS
    def baptis_list(self): return self.list_all("baptis", "id_baptis")
    def baptis_get(self, id_baptis): return self.get_by_id("baptis","id_baptis", id_baptis)
    def baptis_insert(self, data):
        payload = {k: data.get(k) for k in ["id_jemaat","nama_ayah","nama_ibu","nama_wali","tgl_baptis","pelayan","surat_baptis"] if k in data}
        return self.insert("baptis", payload)
    def baptis_update(self, id_baptis, data): data.pop("id_baptis", None); return self.update("baptis","id_baptis", id_baptis, data)
    def baptis_delete(self, id_baptis): return self.delete("baptis","id_baptis", id_baptis)

    # JADWAL_IBADAH
    def jadwal_ibadah_list(self): return self.list_all("jadwal_ibadah", "id_jdl_ibadah")
    def jadwal_ibadah_get(self, id_jdl_ibadah): return self.get_by_id("jadwal_ibadah","id_jdl_ibadah", id_jdl_ibadah)
    def jadwal_ibadah_insert(self, data):
        payload = {k: data.get(k) for k in ["id_jemaat","tgl_ibadah","wilayah","hari_ibadah","jam_ibadah","pemimpin_ibadah"] if k in data}
        return self.insert("jadwal_ibadah", payload)
    def jadwal_ibadah_update(self, id_jdl_ibadah, data): data.pop("id_jdl_ibadah", None); return self.update("jadwal_ibadah","id_jdl_ibadah", id_jdl_ibadah, data)
    def jadwal_ibadah_delete(self, id_jdl_ibadah): return self.delete("jadwal_ibadah","id_jdl_ibadah", id_jdl_ibadah)

    # JEMAAT
    def jemaat_list(self): return self.list_all("jemaat", "id_jemaat")
    def jemaat_get(self, id_jemaat): return self.get_by_id("jemaat","id_jemaat", id_jemaat)
    def jemaat_insert(self, data):
        payload = {k: data.get(k) for k in ["nama_jemaat","jk_jemaat","alamat_jemaat","tempat_lahir","tgl_lahir","no_hp","status_dalam_keluarga","wilayah"] if k in data}
        return self.insert("jemaat", payload)
    def jemaat_update(self, id_jemaat, data): data.pop("id_jemaat", None); return self.update("jemaat","id_jemaat", id_jemaat, data)
    def jemaat_delete(self, id_jemaat): return self.delete("jemaat","id_jemaat", id_jemaat)

    # PENGUMUMAN
    def pengumuman_list(self): return self.list_all("pengumuman", "id_pengumuman")
    def pengumuman_get(self, id_pengumuman): return self.get_by_id("pengumuman","id_pengumuman", id_pengumuman)
    def pengumuman_insert(self, data):
        payload = {k: data.get(k) for k in ["sub_jenis","isi_pengumuman"] if k in data}
        return self.insert("pengumuman", payload)
    def pengumuman_update(self, id_pengumuman, data): data.pop("id_pengumuman", None); return self.update("pengumuman","id_pengumuman", id_pengumuman, data)
    def pengumuman_delete(self, id_pengumuman): return self.delete("pengumuman","id_pengumuman", id_pengumuman)

# Lazy global instance + wrappers
_DB = None
def _db():
    global _DB
    if _DB is None:
        _DB = crud()
    return _DB

def baptis_list(): return _db().baptis_list()
def baptis_get(id_baptis): return _db().baptis_get(id_baptis)
def baptis_insert(data): return _db().baptis_insert(data)
def baptis_update(id_baptis, data): return _db().baptis_update(id_baptis, data)
def baptis_delete(id_baptis): return _db().baptis_delete(id_baptis)

def jadwal_ibadah_list(): return _db().jadwal_ibadah_list()
def jadwal_ibadah_get(id_jdl_ibadah): return _db().jadwal_ibadah_get(id_jdl_ibadah)
def jadwal_ibadah_insert(data): return _db().jadwal_ibadah_insert(data)
def jadwal_ibadah_update(id_jdl_ibadah, data): return _db().jadwal_ibadah_update(id_jdl_ibadah, data)
def jadwal_ibadah_delete(id_jdl_ibadah): return _db().jadwal_ibadah_delete(id_jdl_ibadah)

def jemaat_list(): return _db().jemaat_list()
def jemaat_get(id_jemaat): return _db().jemaat_get(id_jemaat)
def jemaat_insert(data): return _db().jemaat_insert(data)
def jemaat_update(id_jemaat, data): return _db().jemaat_update(id_jemaat, data)
def jemaat_delete(id_jemaat): return _db().jemaat_delete(id_jemaat)

def pengumuman_list(): return _db().pengumuman_list()
def pengumuman_get(id_pengumuman): return _db().pengumuman_get(id_pengumuman)
def pengumuman_insert(data): return _db().pengumuman_insert(data)
def pengumuman_update(id_pengumuman, data): return _db().pengumuman_update(id_pengumuman, data)
def pengumuman_delete(id_pengumuman): return _db().pengumuman_delete(id_pengumuman)
