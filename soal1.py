# Code Latihan 1 di sini
data_kotor = [100, 500, 100, 200, 300, 500, 200]

satu = list(set(data_kotor))
print(f"Data Bersih: {satu}")

satu.sort(reverse=True)
print(f"Data Terbesar ke Terkecil: {satu}")

satu.append(999)
satu.sort(reverse=True)
print(f"Ubah data di urutan pertama: {satu}")