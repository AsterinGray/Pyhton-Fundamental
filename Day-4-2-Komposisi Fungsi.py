def f(x):
    return abs(A*x+B)

N = input().split()

A = int(N[0])
B = int(N[1])
K = int(N[2])
x = int(N[3])

hasil = x
for i in range (0,K):
    hasil = f(hasil)
    
print(hasil)
