n = int(input())

inp = input().split(" ")


nilaiMax = int(inp[0])
nilaiMin = int(inp[0])

for i in range(1, n):
    if (int(inp[i]) > nilaiMax):
        nilaiMax  = int(inp[i])

    if (int(inp[i]) < nilaiMin):
        nilaiMin = int(inp[i])

print(nilaiMax, nilaiMin)
        
