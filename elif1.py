# s=[]


# for i in range(0,5):
#   n=int(input("Enter the integer: "))
#   s.append(n)
  
# print(s)

# for i in range(len(s)-1):
#   if (s[i]>s[i+1]):
#     print(f"largest is {s[i]}")

# s = []

# # Take 5 integer inputs from the user
# for i in range(5):
#     n = int(input("Enter the integer: "))
#     s.append(n)
  
# # Print the list
# print(s)

s = []

# Collect 5 integers from the user
for i in range(5):
    n = int(input("Enter the integer: "))
    s.append(n)
  
# Print the list of entered integers
print(s)

# Find the largest element in the list
largest = max(s)
print(f"The largest element is {largest}")



smallest = min(s)
print(f"The smallest element is {smallest}")

    
    
    