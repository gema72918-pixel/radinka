print("=== PRISMA SEGI ENAM ===")
sisi = float(input("Masukkan panjang sisi: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))

luas_alas = (3 * 1.732 / 2) * sisi * sisi
volume = luas_alas * tinggi_prisma

print("Volume prisma segi enam:", volume)
