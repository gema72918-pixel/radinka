print("=== TABUNG ===")
jari = float(input("Masukkan jari-jari: "))
tinggi = float(input("Masukkan tinggi: "))

phi = 3.14
volume = phi * jari * jari * tinggi
luas_permukaan = 2 * phi * jari * (jari + tinggi)

print("Volume tabung:", volume)
print("Luas permukaan tabung:", luas_permukaan)
