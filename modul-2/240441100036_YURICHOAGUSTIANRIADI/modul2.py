class MataKuliah:
    def __init__(self, kode, nama, sks):
        if MataKuliah.cek_sks_valid(sks):
            self.kode = kode
            self.nama = nama
            self.sks = sks
        else:
            print(f"SKS untuk mata kuliah tidak valid. Hanya boleh 2 atau 3.")
            self.kode = self.nama = None
            self.sks = 0

    @staticmethod
    def cek_sks_valid(sks):
        return sks == 2 or sks == 3


class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if Mahasiswa.validasi_nim(nim):
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            self.matkul_diambil = []
            Mahasiswa.jumlah_mahasiswa += 1
        else:
            print(f"NIM tidak valid untuk mahasiswa. Harus diawali '23' dan 10 digit.")
            self.nama = self.nim = self.prodi = None
            self.matkul_diambil = []

    def tambah_matkul(self, matkul):
        if matkul.sks > 0:
            self.matkul_diambil.append(matkul)

    def tampilkan_info(self):
        if self.nim: 
            print(f"Nama     : {self.nama}")
            print(f"NIM      : {self.nim}")
            print(f"Prodi    : {self.prodi}")
            print("Mata Kuliah Diambil:")
            for matkul in self.matkul_diambil:
                print(f"- {matkul.nama} ({matkul.kode}), {matkul.sks} SKS")
            print()

    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return len(nim) == 10 and nim.isdigit() and nim[:2] == "23"


class Kampus:
    def __init__(self, nama_kampus, alamat):
        if Kampus.validasi_nama_kampus(nama_kampus):
            self.nama_kampus = nama_kampus
            self.alamat = alamat
            Kampus.jumlah_mahasiswa = Mahasiswa.jumlah_mahasiswa
        else:
            print(f"Nama kampus tidak valid. Tidak boleh mengandung angka.")
            self.nama_kampus = self.alamat = "Tidak Valid"

    @classmethod
    def info_kampus(cls, nama):
        print(f"Nama Kampus     : {nama}")
        print(f"Total Mahasiswa : {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama):
        for huruf in nama:
            if huruf.isdigit():
                return False
        return True


mk1 = MataKuliah("SI 101", "Pemrograman", 2)
mk2 = MataKuliah("SI 102", "Struktur Data", 3)
mk3 = MataKuliah("SI 103", "Basis Data", 3)
mk4 = MataKuliah("SI 104", "Jaringan Komputer", 3)
mk5 = MataKuliah("SI 105", "Sistem Operasi", 3)
mk6 = MataKuliah("SI 106", "Kalkulus", 2)
mk7 = MataKuliah("SI 107", "Kecerdasan Buatan", 3)
mk8 = MataKuliah("SI 108", "Pemrograman Web", 3)


m1 = Mahasiswa("Yuricho", "2312345678", "Sistem Informasi")
m2 = Mahasiswa("Agustian", "2312345679", "Sistem Informasi")
m3 = Mahasiswa("Riadi", "2312345680", "Sistem Informasi")
m4 = Mahasiswa("Ahmad", "2312345681", "Sistem Informasi")
m5 = Mahasiswa("Andika", "2312345682", "Sistem Informasi")
m6 = Mahasiswa("Dimas", "2312345683", "Sistem Informasi")


for m in [m1, m2, m3, m4, m5, m6]:
    m.tambah_matkul(mk1)
    m.tambah_matkul(mk2)
    m.tambah_matkul(mk3)
    m.tambah_matkul(mk4)

kampus = Kampus("Universitas Trunojoyo Madura ", "Jl. Telang, No. 4")


print("\n=== Data Mahasiswa ===\n")
for m in [m1, m2, m3, m4, m5, m6]:
    m.tampilkan_info()


print("=== Info Kampus ===\n")
Kampus.info_kampus(kampus.nama_kampus)
print(f"Alamat Kampus       : {kampus.alamat}")
print(f"Validasi Nama Kampus: {Kampus.validasi_nama_kampus(kampus.nama_kampus)}")
