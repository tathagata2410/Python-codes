n=int(input("enter the number: "))
i=0
for i in range(2,n):
  if(n%i==0):
    print("Not prime")
    break
  else:
    print("prime")  
    break