a=int(input("Enter the number :"))

fact=1
if a>=1:
  for  i in range(1,a+1):
    fact=fact*i
  print("factorial num is :",fact)
