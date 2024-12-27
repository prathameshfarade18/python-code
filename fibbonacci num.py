from itertools import count

p=int(input("Enter the number :"))


a=1
b=1

# for i in range(1,p):
 #   print(a,end=" ")
  #  c=a+b
   # a=b
    #b=c


count=0
if p > 0:
    print("fabonacci Number")
    while count<p:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
