n=int(input("enter the number: "))
print(f"Multiplication Table of {n}: ")

for i in range(1,11):
  print(f"{n} * {i} =",n*i)
  i+=1

