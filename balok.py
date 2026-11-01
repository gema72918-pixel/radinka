print("=== BALOK ===")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))

volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("Volume balok:", volume)
print("Luas permukaan balok:", luas_permukaan)
