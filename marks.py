num=int(input("Enter marks: "))
if(num>100):
  print("Not Valid Recheck")
elif(num<100 and num>=90):
   print("EX")  
elif(num<90 and num>=80):
   print("A")
elif(num<80 and num>=70):
   print("B")
elif(num<70 and num>=60):
   print("C")
elif(num<60 and num>=50):
   print("D")
else:
  print("F")