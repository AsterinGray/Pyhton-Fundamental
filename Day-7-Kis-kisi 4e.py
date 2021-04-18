N = int(input())

A = 1
space = N - 1
star = N - (N-1)

for h in range (0,N):
    for i in range (0,space):
        print (" ", end="")
    for j in range (0,star):
        print (A, end="")
        A +=1
        if (A > 9):
            A=1
    space -= 1
    star += 2
    print()
'''
A =1

for baris in range (0,N):
    for spasi in range (0,N-baris-1):
        print(" ",end="")
    for bintang in range (0,(baris+1)*2-1):
        print(A,end="")
        A +=1
        if (A > 9):
            A=1
    print()
'''    
    
