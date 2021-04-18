N = int(input())
M = input().split()
'''
for i in range(0,len(M)):
    M[i] = int(M[i])
'''
st1 = set(M)
    
A = int(input())
B = input().split()
'''
for i in range(0,len(B)):
    B[i] = int(B[i])
'''
st2 = set(B)

st3 = st1 ^ st2
print(len(st3))
    


