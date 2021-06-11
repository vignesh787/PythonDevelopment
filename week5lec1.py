def discount(cost,d):
    ans = cost - (cost * (d/100))
    return ans

print("Enter cost price")
c =int(input())
print("Enter discount")
d=int(input())

print("The final discount is : ",discount(c,d))

