N = int(input())
inp = input().split(" ")

for i in range(N-1, -1, -1):
    print(inp[i], end="")
    if (i > 0):
        print(",",end="")
print()
