N = int(input())
data = input().split()


for i in range (0,N):
    data[i] = int(data[i])
    
avg = sum(data)/len(data)

ct = 0
for i in range (0,N):
    if(data[i] < avg):
        ct += 1
print (ct)

