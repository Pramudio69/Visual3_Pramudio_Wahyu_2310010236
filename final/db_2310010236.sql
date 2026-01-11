-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 10 Nov 2025 pada 07.39
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_2310010236`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `nama_admin` varchar(100) DEFAULT NULL,
  `level` enum('admin','pengurus') DEFAULT 'admin'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `baptis`
--

CREATE TABLE `baptis` (
  `id_baptis` int(11) NOT NULL,
  `id_jemaat` int(11) DEFAULT NULL,
  `nama_ayah` varchar(50) DEFAULT NULL,
  `nama_ibu` varchar(100) DEFAULT NULL,
  `nama_wali` varchar(100) DEFAULT NULL,
  `tgl_baptis` date DEFAULT NULL,
  `pelayan` varchar(100) DEFAULT NULL,
  `surat_baptis` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `jadwal_ibadah`
--

CREATE TABLE `jadwal_ibadah` (
  `id_jdl_ibadah` int(11) NOT NULL,
  `id_jemaat` int(11) DEFAULT NULL,
  `tgl_ibadah` date DEFAULT NULL,
  `wilayah` varchar(30) DEFAULT NULL,
  `hari_ibadah` varchar(30) DEFAULT NULL,
  `jam_ibadah` varchar(20) DEFAULT NULL,
  `pemimpin_ibadah` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `jemaat`
--

CREATE TABLE `jemaat` (
  `id_jemaat` int(11) NOT NULL,
  `nama_jemaat` varchar(100) DEFAULT NULL,
  `jk_jemaat` enum('L','P') DEFAULT NULL,
  `alamat_jemaat` varchar(100) DEFAULT NULL,
  `tempat_lahir` varchar(50) DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `no_hp` varchar(50) DEFAULT NULL,
  `status_dalam_keluarga` varchar(50) DEFAULT NULL,
  `wilayah` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengumuman`
--

CREATE TABLE `pengumuman` (
  `id_pengumuman` int(11) NOT NULL,
  `sub_jenis` varchar(50) DEFAULT NULL,
  `isi_pengumuman` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeks untuk tabel `baptis`
--
ALTER TABLE `baptis`
  ADD PRIMARY KEY (`id_baptis`),
  ADD KEY `id_jemaat` (`id_jemaat`);

--
-- Indeks untuk tabel `jadwal_ibadah`
--
ALTER TABLE `jadwal_ibadah`
  ADD PRIMARY KEY (`id_jdl_ibadah`),
  ADD KEY `id_jemaat` (`id_jemaat`);

--
-- Indeks untuk tabel `jemaat`
--
ALTER TABLE `jemaat`
  ADD PRIMARY KEY (`id_jemaat`);

--
-- Indeks untuk tabel `pengumuman`
--
ALTER TABLE `pengumuman`
  ADD PRIMARY KEY (`id_pengumuman`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `baptis`
--
ALTER TABLE `baptis`
  MODIFY `id_baptis` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `jadwal_ibadah`
--
ALTER TABLE `jadwal_ibadah`
  MODIFY `id_jdl_ibadah` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `jemaat`
--
ALTER TABLE `jemaat`
  MODIFY `id_jemaat` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `pengumuman`
--
ALTER TABLE `pengumuman`
  MODIFY `id_pengumuman` int(11) NOT NULL AUTO_INCREMENT;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `baptis`
--
ALTER TABLE `baptis`
  ADD CONSTRAINT `baptis_ibfk_1` FOREIGN KEY (`id_jemaat`) REFERENCES `jemaat` (`id_jemaat`);

--
-- Ketidakleluasaan untuk tabel `jadwal_ibadah`
--
ALTER TABLE `jadwal_ibadah`
  ADD CONSTRAINT `jadwal_ibadah_ibfk_1` FOREIGN KEY (`id_jemaat`) REFERENCES `jemaat` (`id_jemaat`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
