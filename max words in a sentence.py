def max_words(my_list):
    max=0
    empty=[]
    for i in my_list:
        current=len(i.split(' '))
        if(current>max):
            max=current
    return max
s=[]
l=int(input("enter size of list"))
for i in range(1,l+1):
    n=input("enter the sentence")
    s.append(n)
print("sentence with max words=",max_words(s))
    
