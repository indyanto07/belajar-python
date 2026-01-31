# Code Latihan 1 di sini
data_kotor = [100, 500, 100, 200, 300, 500, 200]

proses = list(set(data_kotor))
proses.sort(reverse=True)
proses.append(999)
proses.sort(reverse=True)
print(f"Data setelah diproses: {proses}")