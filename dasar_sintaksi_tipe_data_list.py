daftar_buku = ['Seven Habits', 'How to Influence People', 'First things First', '4D X']
print("Tampilkan semua daftar buku")
print(daftar_buku)

print('\nproses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan dengan index tettentu')
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Tampilkan dengan format in range, dimana tipe data tipa element berbeda-beda')
daftar_buku = [1, 'kenji volume 2', -3.14, 3.14]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Kembalikan nilai awal daftar buku')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First things First', '4D X']

print(daftar_buku)

print('\n Menambah data')
daftar_buku.append('Dunia Matematika kelas 2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print(daftar_buku)

print('\nhapus data dengan clear')
daftar_buku.clear()
print(daftar_buku)

print('\ndata asli')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First things First', '4D X']
print(daftar_buku)

print('\n data setelah dihapus dengan pop')
daftar_buku.pop(1)
print(daftar_buku)

print('\nperintah del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First things First', '4D X']
del daftar_buku[:]
print(daftar_buku)

'''Perintah list comprehesion'''
print('\nperintah list comprehension')
print('data asli')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First things First', '4D X', 'Good Freelancer Ferdinant']
print(daftar_buku)

'''del daftar_buku[start:stop]
start : data pertama yanga akan di kenai perintah
stop  : banyaknya data yang akan di kenai perintah
'''
print('\nSetelah dengan perintah del')
del daftar_buku[0:-2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print(daftar_buku)
