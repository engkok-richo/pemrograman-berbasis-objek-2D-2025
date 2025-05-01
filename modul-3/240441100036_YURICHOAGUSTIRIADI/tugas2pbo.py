class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "truk":
            return 5
        elif self.jenis_kendaraan == "mobil":
            return 4
        else:
            return 6

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == "citilink":
            return 2
        elif self.maskapai.lower() == "garuda":
            return 3
        else:
            return 4

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat.estimasi_waktu(self)
        waktu_udara = PengirimanUdara.estimasi_waktu(self)
        estimasi_awal = min(waktu_darat, waktu_udara)

        if self.tujuan.lower() not in ["jakarta", "surabaya", "bogor", "bandung"]:
            return estimasi_awal + 3
        else:
            return estimasi_awal
        
    def info(self):
        print(f"\nAsal            : {self.asal}")
        print(f"Tujuan          : {self.tujuan}")
        print(f"Jenis Kendaraan : {self.jenis_kendaraan}")
        print(f"Maskapai        : {self.maskapai}")
        print(f"Estimasi Waktu  : {self.estimasi_waktu()} hari")

pengiriman1 = PengirimanInternasional("Jakarta", "Bandung", "mobil", "Lion Air")
pengiriman2 = PengirimanInternasional("Bogor", "Depok", "truk", "Citilink")
pengiriman3 = PengirimanInternasional("Surabaya", "Malaysia", "truk", "garuda")
pengiriman4 = PengirimanInternasional("Bandung", "Jakarta", "bus", "Citilink")

pengiriman1.info()
pengiriman2.info()
pengiriman3.info()
pengiriman4.info()