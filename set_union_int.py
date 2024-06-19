a={1,22,334,87}
b={1,234,333,87}
print(a.union(b))
print(a.intersection(b))
print(b-a)

c = {1, 2}
print("Is subset_set a subset of Set1?", c.issubset(a))
print("Is Set1 a superset of subset_set?", b.issuperset(c))