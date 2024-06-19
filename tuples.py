a=(1,2,3,4,5)
print(type(a))
#tupple is like string immutable
my_tuple = (1, 2, 2, 3, 4, 4, 4)
count = my_tuple.count(4)
print(count)  # Output: 3


my_tuple = ('a', 'b', 'c', 'd')
index = my_tuple.index('c')
print(index)  # Output: 2

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)    # Output: True
print(67 in my_tuple)    # Output: False
print(6 not in my_tuple)  # Output: True

my_tuple = (0, 1, 2, 3, 4, 5, 6)
sliced_tuple = my_tuple[2:5]
print(sliced_tuple)  # Output: (2, 3, 4)


