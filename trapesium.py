print("=== TRAPESIUM ===")
sisi_atas = float(input("Masukkan sisi atas: "))
sisi_bawah = float(input("Masukkan sisi bawah: "))
tinggi = float(input("Masukkan tinggi: "))
sisi_kiri = float(input("Masukkan sisi kiri: "))
sisi_kanan = float(input("Masukkan sisi kanan: "))

luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
keliling = sisi_atas + sisi_bawah + sisi_kiri + sisi_kanan

print("Luas trapesium:", luas)
print("Keliling trapesium:", keliling)
