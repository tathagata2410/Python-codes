s=[]
for i in range(0,3):
  s.append(input("Enter a string: "))
print(s)  


n=input("enter: ")
for i in range(3):
  if n in s[i]:
    print("found")
  else:
    print("not found")