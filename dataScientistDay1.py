import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data dummy
data = {
    'id_produk': ['P001','P002','P003','P004','P005','P006','P007','P008','P009','P010','P011','P012','P013','P014','P015'],
    'nama_produk': ['Sabun Mandi A','Sampo X','Snack Ring','Minuman Y','Snack Keju','Kopi Hitam','Air Mineral','Pasta Gigi Z',
                    'Snack Ring','Sampo X','Kopi Hitam','Snack Keju','Minuman Y','Air Mineral','Pasta Gigi Z'],
    'kategori': ['Kebutuhan Rumah','Kebutuhan Rumah','Makanan','Minuman','Makanan','Minuman','Minuman','Kebutuhan Rumah',
                 'Makanan','Kebutuhan Rumah','Minuman','Makanan','Minuman','Minuman','Kebutuhan Rumah'],
    'harga': [12000,25000,8000,10000,9500,15000,5000,18000,8000,None,15000,9500,10000,5000,18000],
    'jumlah_terjual': [150,90,300,400,250,180,600,120,310,100,None,250,400,1000,110],
    'kota': ['jakarta','bandung','jakarta','surabaya','jakarta','bandung','surabaya','jakarta','Jakarta','bandung','Surabaya','jakarta','surabaya','surabaya','jakarta'],
    'tanggal': ['2024-01-05','2024-01-07','2024-01-08','2024-01-09','2024-01-10','2024-01-11','2024-01-12','2024-01-13',
                '2024-01-14','2024-01-15','2024-01-16','2024-01-17','2024-01-18','2024-01-19','2024-01-20']
}

# Buat DataFrame
df = pd.DataFrame(data)

# Simpan ke CSV
# df.to_csv("data_penjualan.csv", index=False)
# df.head()   
# df.info()    
# df.shape
# df.describe
# print(df['harga'].mean())      # Rata-rata
# print(df['harga'].median())
# print(df['harga'].mode())

sns.histplot(df['harga'])
plt.title('Distribusi Harga')
plt.show()
