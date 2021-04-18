N = int(input())

'''
space = N - 1
star = N - (N-1)

for h in range (0,N):
    for i in range (0,space):
        print (" ", end="")
    for j in range (0,star):
        print ("*", end="")
    space -= 1
    star += 1
    print("")
'''

for baris in range (0,N):
    for spasi in range (0,N-baris-1):
        print(" ",end="")
    for bintang in range (0,baris+1):
        print("*",end="")
    print()
