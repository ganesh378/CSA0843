a=int(input("enter number"))
b=int(input("enter number"))
choice=int(input("enter choice"))
if(a>0)and(b>0):
    if(choice==1):  
        add=a+b
        print("the addition is",add)
    elif(choice==2):
          sub=a-b
          print("the subtraction is",sub)
    elif(choice==3):
        mul=a*b
        print("the multiplication is",mul)
    elif(choice==4):
          div=a%b
          print("the division is",div)
    else:
        print("invalid choice")
else:
    print("the numbers should be above zero")
