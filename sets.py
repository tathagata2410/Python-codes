ed={}
print(type(ed))



es= set()
print(type(es))
s={1,5,32,4,4,5,5,5,6}
print(s)
s.add(69)
print(s)
s.clear()
print(s)

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set1:", set1)
print("Set2:", set2)

# Adding elements to a set
set1.add(6)
print("Set1 after adding an element:", set1)

# Removing elements from a set
set1.remove(6)
print("Set1 after removing an element:", set1)

# Checking if an element is in a set
print("Is 3 in Set1?", 3 in set1)

# Set operations
# Union
union_set = set1.union(set2)
print("Union of Set1 and Set2:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference of Set1 and Set2:", difference_set)

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of Set1 and Set2:", symmetric_difference_set)

# Subset and Superset
subset_set = {1, 2}
print("Is subset_set a subset of Set1?", subset_set.issubset(set1))
print("Is Set1 a superset of subset_set?", set1.issuperset(subset_set))

# Clearing a set
set1.clear()
print("Set1 after clearing:", set1)
