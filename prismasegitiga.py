print("=== PRISMA SEGITIGA SAMA SISI ===")
sisi_segitiga = float(input("Masukkan sisi segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))

tinggi_segitiga = 0.5 * sisi_segitiga * 1.732
luas_alas = 0.5 * sisi_segitiga * tinggi_segitiga
volume = luas_alas * tinggi_prisma

keliling_alas = 3 * sisi_segitiga
luas_permukaan = (2 * luas_alas) + (keliling_alas * tinggi_prisma)

print("Volume prisma:", volume)
print("Luas permukaan prisma:", luas_permukaan)
