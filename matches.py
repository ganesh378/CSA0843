def diff_position(string1,string2):
	a=string1.replace('  ',' ')
	b=string2.replace('  ',' ')
	if(len(a)<len(b)):
		length=len(a)
	else:
		length=len(b)
	count=0
	for i in range(length):
		if(a[i]!=b[i]):
			count=count+1
	print(length-count)
string1=str(input("enter a string"))
string2=str(input("enter another string"))
diff_position(string1,string2)
