# Set in python are mutable .However , every elements of set must be immutable
# Creating an empty set
a = set()  # This is a proper way of creating an empty set.
# a = {}  # This is not empty set rather it is a dictionary

a = set([1, 2, 3, 4])
print(a)  # {1, 2, 3, 4}

a = {1, 2, "a", "b", "apple", True}
print(a)


# set only takes unique elements
print(set([1, 2, 5, 3, 2, 3, 4, 5])
