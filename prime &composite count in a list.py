mylist = []
n=int(input("enter length of list"))
for a in range(1,n+1):
    e=int(input("enter the elements"))
    mylist.append(e)
print(mylist)
i=len(mylist)
prime=[]
composite=[]
for i in range(0,i):
    c=0
    for j in range(2,mylist[i]):
        if mylist[i]%j==0:
            c=1
            break
    if c==0:
        prime.append(mylist[i])
    else:
        composite.append(mylist[i])
x=len(prime)
print("no of prime numbers=",x)
y=len(composite)
print("no of composite numbers=",y)

