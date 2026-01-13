#operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah dengan assignment

a = 5 #ini adalah assignment
print("nilai a =", a)

a += 1 #ini artinya a = a + 1
print("nilai a += 1 menjadi", a)

a -= 2 #ini artinya a = a - 2
print("nilai a -= 2 menjadi", a)

a *= 5 #ini artinya a = a * 5
print("nilai a *= 5 menjadi", a)

a /= 2 #ini artinya a = a / 2
print("nilai a /= 2 menjadi", a)

b = 10
print("\nnilai b =", b)

#modulus dan floor division
b %= 3 
print("nilai b %= nilai b menjadi", b)

b = 10
print("\nnilai b =", b)

b //= 3
print("nilai b //= nilai b menjadi", b)

#pangkat atau eksponen
a = 5
print("\nnilai a =", a)
a **= 3
print("nilai a **= nilai a menjadi", a)

#operasi bitwise 
#OR
c = True
print("\nnilai c =", c)
c |= False
print("nilai c |= False,nilai c menjadi", c)
c = False
print("\nnilai c =", c)
c |= False
print("nilai c |= False,nilai c menjadi", c)

#AND
c = True
print("\nnilai c =", c)
c &= False
print("nilai c &= False,nilai c menjadi", c)
c = True
print("\nnilai c =", c)
c &= True
print("nilai c &= True,nilai c menjadi", c)

#XOR
c = True
print("\nnilai c =", c)
c ^= False
print("nilai c ^= False,nilai c menjadi", c)
c = True
print("\nnilai c =", c)
c ^= True
print("nilai c ^= True,nilai c menjadi", c)


#geser - geser
d = 0b00001111
print("\nnilai d =", format(d,'08b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi", format(d,'08b'))
d <<= 1 
print("nilai d <<= 1, nilai d menjadi", format(d,'08b'))