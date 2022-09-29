p=int(input("enter amount"))
t=int(input("enter time"))
s=str(input("is the customer a senior citizen"))
yes=1
no=2
if(s==yes):
    print("rate of interest =12%")
    r=12
    si=p*t*r/100
    print("simple interest=",si)
else:
    print("rate of interset =10%")
    r=10
    si=p*t*r/100
    print("simple interest=",si)
