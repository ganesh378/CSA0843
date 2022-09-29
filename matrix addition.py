x=int(input("enter no of rows of matrix a"))
y=int(input("enter no of columns of matrix a"))
matrix1=[]
for i in range(x):
    a=[]
    for j in range(y):
        a.append(int(input("enter the values for matrix1")))
    matrix1.append(a)
for i in range(x):
    for j in range(y):
        print(matrix1[i][j],end=" ")
    print()
p=int(input("enter no of rows of matrix b"))
q=int(input("enter no of columns of matrix b"))
matrix2=[]
for i in range(p):
    b=[]
    for j in range(q):
        b.append(int(input("enter the values for matrix2")))
    matrix2.append(b)
for i in range(p):
    for j in range(q):
        print(matrix2[i][j],end=" ")
    print()
add=[0,0,0],[0,0,0],[0,0,0]
for i in range(x):
    for j in range(len(matrix1[0])):
        add[i][j]=matrix1[i][j]+matrix2[i][j]
        print(add[i][j],end=" ")
     print()
