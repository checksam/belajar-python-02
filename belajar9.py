#latihan logika dan komparasi
#membuat gabungan area rentang dari angka
#+++++++++++3------------10++++++++++++

InputUser = float(input("Masukkan angka yang bernilai kurang\n dari 3 \natau \nlebih besar dari 10\n: "))

#++++++++++++3-------------
#memeriksa angka kurang dari 3
iskurangdari = (InputUser < 3)
print("Kurang dari 3 =", iskurangdari)


#-------------10++++++++++++
#memeriksa angka lebih dari 10
islebihdari = (InputUser > 10)
print("Lebih dari 10 =", islebihdari)

#+++++++++++3------------10++++++++++++

isCorrect = iskurangdari or islebihdari
print("angka yg anda masukkan=", isCorrect)

#-----------3++++++++++++10-----------
#kasus irisan
print("\n,",10*"=","\n")
InputUser = float(input("Masukkan angka yang bernilai lebih\n dari 3 \ndan \nkurang dari 10\n: "))

#-----------3++++++++++++
# lebih dari 3
islebihdari = InputUser > 3
print("Lebih dari 3 =", islebihdari)

#++++++++++++10-----------
# kurang dari 10
iskurangdari = InputUser < 10
print("Kurang dari 10 =", iskurangdari)

#-----------3++++++++++++10-----------
isCorrect = islebihdari and iskurangdari
print("angka yg anda masukkan =", isCorrect)