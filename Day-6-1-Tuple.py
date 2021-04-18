N = int(input())

inp = input().split()

for i in range (0,N):
    inp[i] = int(inp[i])

tup = tuple(inp)

print(hash(tup))
    
    
