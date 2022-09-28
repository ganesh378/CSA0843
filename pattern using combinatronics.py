a=int(input("enter the no of rows"))
b=1
for i in range(1,a+1):
    for space in range(1,a-i+1):
        print(" ",end="")
    for j in range(0,i):
        if j==0 or i==0:
            b=1
        else:
            b=b*(i-j)//j
        print(b,end=" ")
    print()
    
            
