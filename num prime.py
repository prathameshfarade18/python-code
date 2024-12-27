p=int(input("Enter the Num :"))
f=0
for i in range (2,p):
    if p%i==0:
      f=1
      break
if f==1:
    print("not prime num")
else:
    print(" Prime num")