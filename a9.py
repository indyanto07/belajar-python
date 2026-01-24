profil_user = {
    "id": 101,
    "username": "data_ninja",
    "skills": ["Python", "SQL"]
}

# Akses Aman
# print(profil_user["alamat"]) # INI BAKAL ERROR (KeyError)
alamat = profil_user.get("alamat", "Alamat tidak diketahui") # INI AMAN

# Nambah Key Baru
profil_user["level"] = "Senior"

print(f"User Level: {profil_user['level']}")
print(f"Alamat: {alamat}")



# set
id_pengunjung = [1, 2, 3, 1, 2, 4, 5]

# Buang duplikat
unik = set(id_pengunjung)
print(f"Pengunjung Unik: {unik}")

# Operasi Himpunan
karyawan_a = {"Andi", "Budi", "Caca"}
karyawan_b = {"Budi", "Dedi", "Eka"}

# Siapa yang ada di kedua tim? (Intersection)
double_job = karyawan_a.intersection(karyawan_b)
print(f"Double Job: {double_job}")


data_kotor = [100, 500, 100, 200, 300, 500, 200]
satu = set(data_kotor)
print(f"Data Bersih: {satu}")
dua = data_kotor.sort(reverse=True)
print(f"Data Terbesar ke Terkecil: {dua}")
tiga = data_kotor[0]= 999
print(f"Ubah data di urutan pertama: {tiga}")
