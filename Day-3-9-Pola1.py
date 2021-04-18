inp = input().split(" ")

n = int(inp[0])
k = int(inp[1])

for i in range(1, n+1):
    if (i % k == 0):
        print("*", end="")
    else:
        print(i, end="")
        
    if (i < n):
        print(" ", end="")

print()
        
    
