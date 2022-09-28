a=int(input("enter a number"))
b=int(input("enter another number"))
ch=int(input("enter choice"))
if(ch==1):
    print("addition")
    a+b
    print("the addition is",a+b)
elif(ch==2):
    print("subtraction")
    a-b
    print("the subtratcion is",a-b)
elif(ch==3):
    print("division")
    a/b
    print("the division is",a/b)
elif(ch==4):
    print("multiplication")
    a*b
    print("the multiplication is",a*b)
else:
    print("invalid choice")
