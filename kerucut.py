print("=== KERUCUT ===")
jari = float(input("Masukkan jari-jari: "))
tinggi = float(input("Masukkan tinggi: "))
garis_pelukis = float(input("Masukkan garis pelukis: "))

phi = 3.14
volume = (1/3) * phi * jari * jari * tinggi
luas_permukaan = phi * jari * (jari + garis_pelukis)

print("Volume kerucut:", volume)
print("Luas permukaan kerucut:", luas_permukaan)
