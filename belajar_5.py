#data yg dimasukkan pasti string
data = input("Masukkan data: ")

print("Data =", data, "type =", type(data))

#jika kita ingin mngambil float,maka
angka_float = float(input("Masukkan angka: "))
print("angka =", angka_float, "type =", type(angka_float))

#jika kita ingin mengambil integer,maka
angka = int(input("Masukkan angka: "))
print("data =", angka, "type =", type(angka))

#bagaimana jika ingin mengambil boolean
biner = bool(int(input("Masukkan nilai boolean: ")))

print("data =", biner, "type =", type(biner))