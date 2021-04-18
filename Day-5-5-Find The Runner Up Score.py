n = int(input())
inp = input().split()

data=[]

for i in range(0,n):
    data.append(int(inp[i]))

data.sort()

#Cari Nilai Terbesar Kedua

hasil = data[len(data)-1] #AmbilAngkaPalingBelakang

for i in range(len(data)-1, -1, -1):
    if (hasil != data[i]):
        hasil = data[i]
        break
    
print(hasil)
