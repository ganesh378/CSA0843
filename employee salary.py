g=int(input("enter the grade of the employee"))
s=int(input("enter salary of employee"))
if(s<10000):
    print("extra 2% bonus")
    b1=s*7//100
    b2=s*12//100
if(g==1 and s>10000):
    print("bonus is 5%")
    bonus=s*5//100
    print("bonus is",bonus)
    ts=s+bonus
    print("total salary is",ts)
elif(g==2 and s>10000):
    print("bonus is 10%")
    bonus=s*10//100
    print("bonus is",bonus)
    ts=s+bonus
    print("total salary is",ts)
elif(g==1 and s<10000):
    print("bonus is 7%")
    ts=s+b1
    print("total salary is",ts)
elif(g==2 and s<10000):
    print("bonus is 12%")
    ts=s+b2
    print("total salary is",ts)
    
