n=int(input("enter the number"))
fact=1
factors=0
if(n==0):
    print("factorial is 1")
elif(n>0):
    while(n!=0):
        fact=fact*n
        n=n-1
    print("the factorial is",fact)
else:
    print("enter positive numbers only")
for i in range(1,n+1):
    if(n%i==0):
        factors=+1
print("the no of factors are",factors)
