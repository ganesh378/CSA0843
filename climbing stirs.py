def climbstairs(n):
    if n<2:
        return 1
    else:
        a=climbstairs(n-1)+climbstairs(n-2)
        return a
n=int(input("enter the no of stairs"))
print("possibilities are",climbstairs(n))
