# add method
s = {1, 2, 3}
result = s.add(4)
print(result)  # None,; because add() method returns nothing.
print(s)   # {1, 2, 3, 4}


# update method
s = {1, 2, 3}
s.update([4, 5, 6, 7])
print(s)  # {1, 2, 3, 4, 5, 6, 7}

# discard method
s = {1, 2, 3, 4}
s.discard(2)
print(s)  #{1, 3, 4}


# remove method
s = {1, 2, 3, 4}
s.remove(2)
print(s)  # {1, 3, 4}


# clear()
s = {1, 2, 3, 4}
s.clear()
print(s)  # {}

# pop()
s = {1, 2, 3}
print(s.pop())  # it randomly pops out  any one value  of the set

# difference()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.difference(b)  # a - b
print(result)  # {3, 4}
print(a - b)  # -operator can be used

# union()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))  # (1, 2, 3, 4, 5, 6}

# issubset()
a = {4, 5, 6}
b = {5, 6, 7, 8, 9}
print(a.union(b))


# Intersection()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b))  # {3, 4}
print(a & b)  # {3, 4}

# symmetric difference()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.symmetric_difference(b)
print(result)  # {1, 2, 5, 6}


# symmetric_difference_update()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.symmetric_difference_update(b)
print(a)  # {1, 2, 5, 6}