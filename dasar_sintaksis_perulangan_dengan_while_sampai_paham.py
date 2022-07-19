# Program Perulangan membaca bukuh dengan while

jumlah_buku = 100
print('Ibu berkata, "baca semua bukumu"')
total_jumlah_baca = 0

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f"jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}")

while total_jumlah_baca < jumlah_buku * 2 :
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} belum dipahami")
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f"jumlah buku yang sudah di baca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}")