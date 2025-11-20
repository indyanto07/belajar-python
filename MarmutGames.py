import random 

welcome_message = "WELCOME TO MARMUT GAMES !"
marmut_posisi = random.randint(1, 4)


print("===============================")
print(f"== {welcome_message} ==")
print("===============================")

nama_user = input("Masukkan Nama Kamu : ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4
goa_awal = " " .join(goa_kosong)
goa = goa_kosong.copy()
goa[marmut_posisi - 1] = "|0_0|"
goa_hasil = " " .join(goa)

print(f'''
Hallo {nama_user}!! Coba Perhatikan Goa dibawah ini

{goa_awal}   
   
''')
pilihan_user = int(input("Menurut kamu di goa berapa MARMUT berada? [1 / 2 / 3 / 4]:  "))

konfirmasi = input(f'''                      
Apakah kamu yakin, nomor {pilihan_user} adalah jawabannya?? [yes/no]:  ''')
                       
    
if konfirmasi == "yes":
    if pilihan_user == marmut_posisi:
        print(f'''
Wowww selamat {nama_user} kamuu menang!! posisis MARMUT ada di goa ke {marmut_posisi} dan pilihanmu adalah {pilihan_user}
{goa_hasil}
          ''')
    else:
       print(f'''
Yahhhh kamuu kalah, MARMUT ada di goa ke {marmut_posisi} sedangkan kamu memilih goa ke {pilihan_user}
{goa_hasil}
          ''')
elif konfirmasi == "no":
        print("program berhenti")
        exit()
else:
        print("input tidak valid, selahkan ulangi program!")
        exit()
        
        




