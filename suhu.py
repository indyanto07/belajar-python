#latihan koversi ssatuan temperatur

# program konversi celcius
print("\nPROGRAM KONVERSI TEMPERATURE \n")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah",celcius, "Celcius")

# Reamur
Reamur = 4 / 5 * celcius
print("suhu dalam reamur adalah",Reamur, "reamur")

#fahrenheit
fahrenheit = 9 / 5 * celcius + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "fahrenhrit")

#kelvin
kelvin = 273 + celcius
print("suhu dalam kelvin adalah",kelvin, "kelvin")

#PR
arsen = float(input('Masukkan suhu yg akan dirubah ke kelvin : '))
xy = (arsen - 32) * 5 / 9
print("suhu dalam kelvin adalah", xy + 273,"kelvin")

andre = float(input('Masukkan suhu yang akan dirubah ke fahreinheit : '))
abc = andre - 273
print("suhu dalam fahrenheit adalah", abc * 9 / 5 + 32,"fahrenheit")

