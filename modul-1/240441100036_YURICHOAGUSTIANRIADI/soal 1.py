# soal 1
class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(self.nama, "sedang berjalan.")

    def berlari(self):
        print(self.nama, "sedang berlari.")

manusia1 = manusia("yuricho", 19, "sumenep")
manusia2 = manusia("tegas", 20, "pasean")
manusia3 = manusia("fauzan", 18, "pamekasan")
manusia4 = manusia("andre", 19, "sumenep")
manusia5 = manusia("agustian", 17, "masalembu")

manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()

# soal 2
class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Alamat  : {self.alamat}\n")

mahasiswa_list = []
for i in range(3):
    print(f"Masukkan data mahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    jurusan = input("Jurusan: ")
    alamat = input("Alamat: ")
    print()
    
    mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    mahasiswa_list.append(mahasiswa)

print("\nData Mahasiswa:")
for mahasiswa in mahasiswa_list:
    mahasiswa.tampilkan_info()

# # soal 3
# class Kucing:
#     def __init__(self, nama, warna, umur):
#         self.nama = nama
#         self.warna = warna
#         self.umur = umur
#     def bersuara(self):
#         print(f"{self.nama} (kucing)")
#         print(f"-warna : {self.warna}")
#         print(f"-umur : {self.umur} tahun")
#         print(f"-suara : mengeong\n")

# class Anjing:
#     def __init__(self, nama, warna, ras):
#         self.nama = nama
#         self.warna = warna
#         self.ras = ras

#     def menggonggong(self):
#         print(f"{self.nama} (Anjing)")
#         print(f"- Warna : {self.warna}")
#         print(f"- Ras   : {self.ras}")
#         print(f"- Suara : Menggonggong\n")

# class Burung:
#     def __init__(self, nama, jenis, warna):
#         self.nama = nama
#         self.jenis = jenis
#         self.warna = warna

#     def berkicau(self):
#         print(f"{self.nama} (Burung)")
#         print(f"- Jenis : {self.jenis}")
#         print(f"- Warna : {self.warna}")
#         print(f"- Suara : Berkicau\n")


# # Membuat objek menggunakan looping
# hewan_list = [
#     Kucing("Milo","hitam putih","2"),
#     Anjing("Buddy","coklat", "buldog"),
#     Burung("Koko", "Beo nias", "hitam")
# ]

# for hewan in hewan_list:
#     if isinstance(hewan, Kucing):
#         hewan.bersuara()
#     elif isinstance(hewan, Anjing):
#         hewan.menggonggong()
#     elif isinstance(hewan, Burung):
#         hewan.berkicau()
