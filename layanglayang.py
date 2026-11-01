print("=== LAYANG-LAYANG ===")
diagonal1 = float(input("Masukkan diagonal 1: "))
diagonal2 = float(input("Masukkan diagonal 2: "))
sisi_pendek = float(input("Masukkan sisi pendek: "))
sisi_panjang = float(input("Masukkan sisi panjang: "))

luas = 0.5 * diagonal1 * diagonal2
keliling = 2 * (sisi_pendek + sisi_panjang)

print("Luas layang-layang:", luas)
print("Keliling layang-layang:", keliling)
