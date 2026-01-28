class mobil:
    def __init__(self,warna,merk,tahun,kecepatan):
        self.warna = warna
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan
        
    def maju(self):
        self.kecepatan += 30
    
    def suara():
        print("brum brum")
    
class sportcar(mobil):
        def turbo(self):
            self.kecepatan += 70
        def tambah_kecepatan(self):
            super().maju()
            print("kecepatan bertambah dari mobil biasa")
            