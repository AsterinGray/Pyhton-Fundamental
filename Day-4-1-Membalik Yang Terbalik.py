def rev(bil):
    hasil = 0
    while (bil > 0):
        digitTerakhir = bil%10
        hasil = hasil*10 + digitTerakhir
        bil //= 10
    return hasil


inp = input().split()

angka1 = int(inp[0])
angka2 = int(inp[1])

angka3 = rev(angka1) + rev(angka2)

print(rev(angka3))


