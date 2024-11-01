# lapy02

# Flowchart Diskon Tiket
![flowchart](   .png)

# Flowchart Kalkulator
![flowchart](   .png)






# Progam Harga Tiket
   # Codingan
'''python
reguler = 50000
vip = 100000
discount = 0.2

tipe_tiket = input('tipe tiket(reguler/vip :)' )
status_member = input('apakah mempunyai member(iya/tidak :)')

if tipe_tiket == 'reguler':
    harga_tiket = reguler
elif tipe_tiket == 'vip':
    harga_tiket = vip
else :
    print('tiket tidak valid')
    exit()

print(f"harga_tiket {harga_tiket}")

# Penjelasan:
Berikut adalah penjelasan tentang kode yang Anda berikan:

1. Inisialisasi Variabel:
   python
   reguler = 50000
   vip = 100000
   discount = 0.2
   
   - reguler: Harga tiket reguler adalah 50.000.
   - vip: Harga tiket VIP adalah 100.000.
   - discount: Diskon yang diatur (20%) tetapi saat ini belum digunakan dalam kode.

2. Input Pengguna:
   python
   tipe_tiket = input('tipe tiket(reguler/vip :)')
   status_member = input('apakah mempunyai member(iya/tidak :)')
   
   - Kode ini meminta pengguna untuk memasukkan jenis tiket yang ingin dibeli (apakah reguler atau VIP) dan apakah mereka memiliki status anggota (member) atau tidak.

3. Penentuan Harga Tiket:
   python
   if tipe_tiket == 'reguler':
       harga_tiket = reguler
   elif tipe_tiket == 'vip':
       harga_tiket = vip
   else:
       print('tiket tidak valid')
       exit()
   
   - Kode ini memeriksa jenis tiket yang dimasukkan pengguna.
   - Jika pengguna memilih 'reguler', harga tiket ditetapkan ke nilai reguler (50.000).
   - Jika pengguna memilih 'vip', harga tiket ditetapkan ke nilai vip (100.000).
   - Jika pengguna memasukkan nilai selain 'reguler' atau 'vip', program mencetak pesan bahwa tiket tidak valid dan keluar dari program.

4. Output Harga Tiket:
   python
   print(f"harga_tiket {harga_tiket}")
   
   - Kode ini mencetak harga tiket yang telah ditentukan berdasarkan input pengguna.

Kesimpulan
Program ini sederhana, meminta pengguna memilih jenis tiket dan memvalidasi pilihan tersebut sebelum mencetak harga tiket yang sesuai. Namun, meskipun ada variabel untuk diskon, diskon tersebut tidak diterapkan dalam kode saat ini.


