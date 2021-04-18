'''
Task 1 : Nilai >= 75, Lulus, Dibawah,
    Tidak Lulus'

Task 2 : Lakukan Pembatasan         

'''

nilai = int(input("Masukan Nilai Anda: "))

if (nilai >= 75 and nilai <= 100):
    print("Lulus")
elif (nilai >= 0 and nilai <= 75):
    print("Tidak Lulus")
else:
    print("Anda salah memasukkan Nilai")
    
