n=int(input("enter the no of elements in a list"))
a=[]
for i in range(0,n):
    elements=input("enter the elements in a list")
    a.append(elements)
print("the list is",a)
min_ele=a[0]
max_ele=a[0]
for i in range(1,len(a)):
    if a[i]<min_ele:
        min_ele=a[i]
    if a[i]>max_ele:
        max_ele=a[i]
b=sorted(a)
m=int(input("enter the mth max number"))
c=b[-m]
print("the mth maximum number is ",c)
n=int(input("enter the nth min number"))
d=b[n+1]
print("the nth minimum number is",d)
add=c+d
print("the sum of m & n is",add)
diff=c-d
print("the difference of m & n is",diff)
