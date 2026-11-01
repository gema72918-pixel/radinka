print("=== PRISMA SEGITIGA ===")
alas_segitiga = float(input("Masukkan alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))
sisi1 = float(input("Masukkan sisi 1 segitiga: "))
sisi2 = float(input("Masukkan sisi 2 segitiga: "))
sisi3 = float(input("Masukkan sisi 3 segitiga: "))

luas_alas = 0.5 * alas_segitiga * tinggi_segitiga
volume = luas_alas * tinggi_prisma
keliling_alas = sisi1 + sisi2 + sisi3
luas_permukaan = (2 * luas_alas) + (keliling_alas * tinggi_prisma)

print("Volume prisma:", volume)
print("Luas permukaan prisma:", luas_permukaan)
