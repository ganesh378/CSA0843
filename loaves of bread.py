a=int(input("enter total no of fresh loaves of bread"))
b=int(input("enter total no of old loaves of bread"))
if(a>=0):
    print("regular price of bread of bread is : 185.00")
    c=float(a*185)
    print("total amount for fresh loaves is",c)
    d=0.6*185
    e=float(b*d)
    print("total amount for old loaves is",e)
    total=c+e
    print("total amount is",total)
else:
    print("invlid values")
