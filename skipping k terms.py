m=int(input("enter the starting value"))
n=int(input("enter the ending value"))
k=int(input("enter the skipping value"))
k+1
if(m>n):
    print("invalid input")
else:
    while(m<n and k>0):
        m=m+k
        print(m)
