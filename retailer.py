a=int(input("enter the no of items"))
def cost(x):
    if x==1:
        print("the shipping charges are",750)
    else:
        print("the shipping charges are",750+(x-1)*200)
cost(a)
