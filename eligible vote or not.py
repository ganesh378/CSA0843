age=int(input("enter age"))
if(age>=18):
    print("person is eligible for vote")
else:
    print("person is not eligible for vote")
    b=18-age
    print("person can be eligible for vote after",b,"years")
