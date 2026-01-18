for i in range(1,11,5):
    print(i)

for i in range(1,6):
    for j in range(1,3):
        print(i,j)
    print('----')
    
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))
    
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

evenNumber = [i for i in range(0, 501, 2)]

angka =[1,2,3,4,5]

for i in range (len(angka)):
    now = angka[i]
    next = i+1

    if next < len(angka):
        printnext = angka[next]
    else:
        printnext = 'ga ada angka lagi bang'
    print(f'angka sekarang {now}, angka selanjutnya {printnext}')