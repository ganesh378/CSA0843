def lolw(a):
  w=a.split()
  if len(w)==0:
      return 0
  return len(w[-1])
a=str(input("enter a string"))
print("length of last words=",lolw(a))
