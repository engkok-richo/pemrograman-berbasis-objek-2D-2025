class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print(f"\nNama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")
        print(f"Tunjangan: {self.tunjangan}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print(f"\nNama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")
        print(f"Jam Kerja per Hari: {self.jam_kerja}")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()

k1 = KaryawanTetap("Richo", 5000000, "IT", 2000000)
k2 = KaryawanTetap("Yuricho", 4500000, "HRD", 1500000)
k3 = KaryawanHarian("Agustian", 3000000, "Produksi", 9)
k4 = KaryawanHarian("Riadi", 2200000, "HRD", 7)

manajemen.tambah_karyawan(k1)
manajemen.tambah_karyawan(k2)
manajemen.tambah_karyawan(k3)
manajemen.tambah_karyawan(k4)

manajemen.tampilkan_semua_karyawan()