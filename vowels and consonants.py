A=input("enter the string")
for i in A:
     if i in "AEIOUaeiou":
         print("\nvowels:",i)
else:
    for i in A:
        if i not in "AEIOUaeiou":
            print("\nconsonant:",i)
         
