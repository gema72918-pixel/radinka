print("=== LIMAS SEGITIGA ===")
alas = float(input("Masukkan alas segitiga: "))
tinggi_alas = float(input("Masukkan tinggi segitiga alas: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))

luas_alas = 0.5 * alas * tinggi_alas
volume = (1/3) * luas_alas * tinggi_limas

print("Volume limas segitiga:", volume)
