N = int(input())
M = input().split()

for i in range(0,N):
    M[i] = int(M[i])
    
st = set(M)

K = int(input())
for i in range (0,K):
    inp = input().split()
    if (inp[0] == "discard"):
        st.discard(int(inp[1]))
    elif (inp[0] == "remove"):
        st.remove(int(inp[1]))
    elif (inp[0] == "pop"):
        st.pop()

print(sum(st))
    
