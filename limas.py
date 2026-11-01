print("=== LIMAS SEGIEMPAT ===")
sisi_alas = float(input("Masukkan sisi alas persegi: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga sisi: "))

luas_alas = sisi_alas * sisi_alas
volume = (1/3) * luas_alas * tinggi_limas
luas_sisi_tegak = 4 * (0.5 * sisi_alas * tinggi_segitiga)
luas_permukaan = luas_alas + luas_sisi_tegak

print("Volume limas:", volume)
print("Luas permukaan limas:", luas_permukaan)
