'''
def case1(N):
    return N%400== 0

def case2(N):
    return(N%4==0 and N%100 != 0)


N = int(input())

if (case1 or case2):
    print("Kabisat")
else:
    print("Bukan Kabisat")
'''

def is_leap(year):
    if (year%400 == 0 or (year%4==0 and year%100 != 0)):
        return True
    else:
        return False


year = int(raw_input())
print is_leap(year)
