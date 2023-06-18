# DangQuocToan_20051051_51
import math
n  = int(input("Enter Prime: "))
List = []
def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
sum = 0
for i in range(2,n+1):
    if isPrime(i) == True:
        List.append(i)
print("All Prime < n: ", List)
for i in List:
    sum += i 
print("Sum = ", sum)
