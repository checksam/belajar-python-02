from datetime import date

nama = input("Masukkan nama: ")
print("nama =", nama, "type =", type(nama))

tempat = input("Masukkan tempat: ")
print("tempat =", tempat, "type =", type(tempat))

tgl_lahir_str = input("Masukkan tanggal lahir (DD/MM/YYYY): ")                                                                                #menginput tgl lahir dgn format string
hari, bulan, tahun = map(int, tgl_lahir_str.split('/'))                                                                                       #memecah string tgl lahir menjadi integer
tanggal_lahir = date(tahun, bulan, hari)                                                                                                      #membuat objek date dari nilai integer
print("Tanggal lahir Anda:", tanggal_lahir.strftime("%d %B %Y"), "type =", type(tanggal_lahir))                                               #menampilkan tgl lahir dgn format yg lebih mudah dibaca

alamat = input("Masukkan alamat: ")
print("alamat =", alamat, "type =", type(alamat))

asal_sekolah = input("Masukkan asal sekolah: ")
print("asal sekolah =", asal_sekolah, "type =", type(asal_sekolah))

jarak_rumah_ke_sekolah = float(input("Masukkan jarak rumah ke sekolah (dalam km): "))
print("jarak rumah ke sekolah =", jarak_rumah_ke_sekolah, "type =", type(jarak_rumah_ke_sekolah))

pekerjaan_ayah = input("Masukkan pekerjaan ayah: ")
print("pekerjaan ayah =", pekerjaan_ayah, "type =", type(pekerjaan_ayah))

gaji_ayah = int(input("Masukkan gaji ayah: "))
print("gaji ayah =", gaji_ayah, "type =", type(gaji_ayah))

pekerjaan_ibu = input("Masukkan pekerjaan ibu: ")
print("pekerjaan ibu =", pekerjaan_ibu, "type =", type(pekerjaan_ibu))

gaji_ibu = int(input("Masukkan gaji ibu: "))
print("gaji ibu =", gaji_ibu, "type =", type(gaji_ibu))