def swap(p1, b1, p2, b2):
    global ls
    temp = ls[p1][b1]
    ls[p1][b1] = ls[p2][b2]
    ls[p2][b2] = temp

def cek():
    global inp
    if (inp[0] == 'A'):
        p1 = 0
    else:
        p1 = 1
    if (inp[2] == 'A'):
        p2 = 0
    else:
        p2 = 1 
    swap(p1, int(inp[1])-1, p2, int(inp[3])-1)

n = int(input())

ls = [[], []]

inp = input().split(" ")
for i in range(0, n):
    ls[0].append(int(inp[i]))

inp = input().split(" ")
for i in range(0, n):
    ls[1].append(int(inp[i]))


q = int(input())
for i in range(0, q):
    inp = input().split(" ")
    cek()
    
for i in range(0, 2):
    for j in range(0, n):
        print(ls[i][j], end="")
        if (j < n-1):
            print(" ", end="")
    print()

