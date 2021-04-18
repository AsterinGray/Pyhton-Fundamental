N = int(input())
inp1 = input().split()
for i in range (0,N):
    inp1[i] = int(inp1[i])
st1 = set(inp1)

M = int(input())
inp2 = input().split()
for i in range (0,M):
    inp2[i] = int(inp2[i])
st2 = set(inp2)

print(st1.issubset(st2))
