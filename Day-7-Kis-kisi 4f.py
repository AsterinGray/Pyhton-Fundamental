N = int(input())
M = N*2-1
K = 0
L = M-1

for i in range (0,M):
    for j in range (0,M):
        if (j == K):
            print("#",end="")
        elif (j == L):
            print("#",end="")
        else :
            print(".",end="")
    K += 1
    L -= 1
    print()


for i in range (0,M):
    for j in range (0,M):
        if (i == j):
            print("#", end="")
        elif(M-1-j == i):
            print("#", end="")
        else :
            print(".",end="")
    print()
