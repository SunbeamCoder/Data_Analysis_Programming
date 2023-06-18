# DangQuocToan_20051051_51
import math
n  = int(input("Enter Prime: "))
if n<0:
    print("Number < 0")
elif n<2:
    print(f"{n} Not isPrime")
else: 
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            print(f"{n} Not isPrime")
            break
    else:
        print(f"{n} isPrime")
            
