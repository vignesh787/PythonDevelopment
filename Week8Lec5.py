import time

def sumOfNNumbers(n):
    sum=0
    for i in range(n):
        sum+=i
    return sum
a=time.time()
print(sumOfNNumbers(100000))
b=time.time()
print(b-a)