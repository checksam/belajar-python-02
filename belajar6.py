#operasi aritmatika
a = 10
b = 3

#operasi tambah +
hasil = a + b
print(a,'+',b,'=', hasil)

#operasi kurang -
hasil = a - b
print(a,'-',b,'=', hasil)

#operasi kali *
hasil = a * b
print(a,'*',b,'=', hasil)

#operasi bagi /
hasil = a / b
print(a,'/',b,'=', hasil)  #hasilnya float

#operasi eksponen  (pangkat) **
hasil = a ** b
print(a,'**',b,'=', hasil)

#operasi floor division  //
hasil = a // b
print(a,'//',b,'=', hasil)  #hasilnya integer

#operasi modulus %
hasil = a % b
print(a,'%',b,'=', hasil)  

#prioitas operasi , operacional precedence
...
 1. ()
 2. eksponen **
 3. perkalian dan temannya *, /, //, %
 4. pertambahan dan pengurangan +, -
...
x = 3
y = 2
z = 4

hasil = x + y * z
print(x,'**',y,'*',z,'+',x,'/',y,'-','%',z,'//',x,'=', hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=', hasil)
#kurung akan mengambil langkah pertama
hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=', hasil)
