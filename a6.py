Matriks = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(Matriks) - 2):
    for j in range(len(Matriks[i])):
        print(f'angka {Matriks[i][j]} {Matriks[i+1][j]} {Matriks[i+2][j]}')