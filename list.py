friends= ["Apple","Orange",5,345.56,False,"Akash","Rohan"]
print(friends[0])
friends[0]="tunai"
print(friends[0])

 
# list are mutable enough  

print(friends[0:4])
print(friends[2:5])


friends.append("ghosh")
print(friends[0:8])



l1=[1,34,56,78,12,2,34,56,777,0]
l1.sort()
l1.reverse()
l1.insert(3,69)  
# index 3,value 69
print(l1)
print(l1.pop(0))
l1.pop(0)



print(l1)
l1.remove(56)
print(l1)
l1.remove(34)
print(l1)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]


my_list = ['a', 'b', 'c', 'd']
index = my_list.index('c')
print(index)  # Output: 2


my_list = [1, 2, 2, 3, 4, 4, 4]
count = my_list.count(4)
print(count)  # Output: 3


my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)  # Output: []


my_list = [1, 2, 3, 4]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3, 4]





