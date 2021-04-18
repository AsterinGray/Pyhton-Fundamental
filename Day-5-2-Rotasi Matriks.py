inp = input().split(" ")

n = int(inp[0])   #Baris 
m = int(inp[1])   #Kolom

matriks  = []
listTemp = []

for baris in range (0,n):
    inp = input().split(" ")
    listTemp.clear()
    for kolom in range(0,m):
        listTemp.append(int(inp[kolom]))
    matriks.append(list(listTemp))

for kolom in range(0, m):
    for baris in range(n-1, -1, -1):
        print(matriks[baris][kolom], end="")
        if (baris > 0):
            print(" ",end="")
    print()
                        
        

