from b1 import mobil, sportcar

sportcar1 = sportcar('merah','toyota',2022,170)
sportcar2 = sportcar('merah','toyota',2022,90)
mobil2 = mobil('biru','bmw',2021,180)
# print(sportcar1.warna,sportcar1.merk,sportcar1.tahun)
# print('-------')
# print(sportcar1.kecepatan)
sportcar1.maju()
print(sportcar1.kecepatan)
mobil.suara()
sportcar1.turbo()
print('sportcar')
print(sportcar1.kecepatan)
print('sportcar 2')
sportcar2.tambah_kecepatan()
print(sportcar2.kecepatan)
# mobil1.warna = 'merah'
# print(mobil1.warna)

# mobil2.warna = 'biru'
# print(mobil2.warna)

