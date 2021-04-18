N = int(input())

if(N >= 0 and N <=100):
    if (N > 85):
        print("Grade: A")
    elif (N > 70):
        print("Grade: B")
    elif (N > 50):
        print("Grade: C")
    else:
        print ("Grade: D")
else:
    print("Inputan Nilai Salah")
