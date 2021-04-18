#Buat Program mengenal Grade Nilai
#A: 85 - 100
#B: 70 - 84
#C: 60 - 69
#D: < 60

nilai = int(input("Silahkan Masukan Nilai Anda: "))

if (nilai >=0 and nilai <= 100):
    if (nilai >= 85):
        print("Grade Anda : A")
    elif (nilai >= 70):
        print("Grade Anda : B")
    elif (nilai >= 60):
        print("Grade Anda : C")
    else:
        print("Grade Anda : D")

    if (nilai % 2 == 0):
        print("Nilai anda adalah Ganjil")
    else:
        print("Nilai anda adalah Ganjil")
else:
    print("Anda Salah Memasukkan Nilai!")
