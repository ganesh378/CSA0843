a=int(input("enter first number"))
b=int(input("enter second number"))
x=a
y=b
while(b!=0):
    t=b
    b=a%b
    a=t
gcd=a
print("gcd is",gcd)
lcm=(x*y)//gcd
print("lcm is",lcm)
