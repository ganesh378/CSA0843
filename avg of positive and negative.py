pos_num=0
no_pos_num=0
neg_num=0
no_neg_num=0
arr=[]
tot=0
print("enter -1 to stop entering")
while(arr!=-1):
    arr=int(input("enter the elements "))
    if(arr==-1):
        print("end of program")
        break
    if(arr==0):
        print("not positive nor negative")
    elif(arr>0):
        pos_num=pos_num+arr
        no_pos_num+=1
        avg=pos_num/no_pos_num
    else:
        neg_num=neg_num+arr
        no_neg_num+=1
        avgn=neg_num/no_neg_num
        
print("average of positive numbers is ",avg)
print("average of negative numbers is",avg)
