print("=== KERUCUT TERPANCUNG ===")
jari_besar = float(input("Masukkan jari-jari besar: "))
jari_kecil = float(input("Masukkan jari-jari kecil: "))
tinggi = float(input("Masukkan tinggi: "))

phi = 3.14
volume = (1/3) * phi * tinggi * (jari_besar * jari_besar + jari_besar * jari_kecil + jari_kecil * jari_kecil)

print("Volume kerucut terpancung:", volume)
