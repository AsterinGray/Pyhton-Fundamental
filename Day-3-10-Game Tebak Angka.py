#Game Tebak Angka

import random

jawaban = 'Y'

while(jawaban == 'Y'):

    print("======================================")
    print("| SELAMAT BERMAINDI GAME TEBAK ANGKA |")
    print("======================================")

    print("\nSilahkan Pilih Tingkat Kesulitan:")
    print("1. Easy\t\t(1-10)")
    print("2. Medium\t(1-100)")
    print("3. Hard\t\t(1-1000)")
    tingkat = int(input("Pilihan(1/2/3): "))

    if (tingkat == 1):
        btsAtas = 10
    elif (tingkat == 2):
        btsAtas = 100
    else:
        btsAtas = s1000
    

    btsBawah = 1
    btsAtas = 100
    nyawa = 15

    angkaAcak = random.randint(btsBawah, btsAtas)

    tebakan = -1

    while (tebakan != angkaAcak and nyawa > 0):
        tebakan = int(input("Masukan Tebakan Anda: "))

        if (tebakan < angkaAcak):
            print("Tebakan Anda Terlalu Kecil")
        elif(tebakan > angkaAcak):
            print("Tebakan Anda Terlalu Besar")
        else:
            print("Selamat Anda berhasil Menebak!")
        print("Sisa Nyawa Anda: ", nyawa)
        print()

    if (nyawa == 0):
        print("Maaf, Anda Gugur")
    jawaban = input("Apakah Anda Masih Ingin Bermain? (Y/N): ")
    jawaban = jawaban.upper()

print("Terima Kasih Telah Memainkan Permainan Ini")
                        
                 


