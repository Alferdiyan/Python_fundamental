#Squenial Sintak

print('Ibu berkata,  "pergi ke toko"')
print('Budi menjawab, "baik, apa yag harus aku lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telur beli 6"')
print("Maka Budi pergi ke toko")
print("dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 10
jumlah_telur = 0
print(fr"jumlah botol susu {jumlah_botol_susu} botol")
print(fr"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0 :
    print("Budi mengecek harga, dan uangnya cukup")
    if jumlah_telur == 0 :
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi Pulang Kerumah")
print("Budi memberikan hasilnya kepada ibu")