N = int(input())


km = N//100000
m = (N%100000) // 100
cm = N%100

print(km, "km")
print(m, "m")
print(cm, "cm")
