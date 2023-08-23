# Creating a non -empty tuples
a = (1, 2, "a", "i", [1, 3])  # Tuple elements are enclosed in parenthesis or small brackets
print(a)
a = tuple([1, 2, 4])
print(a)  # (1, 2, 3)


# unpacking
a, b = 1 , 2
print(a)  # 1; integer type
print(b)  # 2; integer type

a, b , c = 2, "hello", ["a", "e", "i"]
print(a)  # 2
print(b)  # hello
print(c)  # ["a", "e", "i"]

# if number of elements in LHS is not equal to RHS then it raises error in tuple unpacking
a, b = 2, "hello", ["a", "e", "i"]
print(a)  # it raises error as there is too much value to unpack
print(b)
print(c)

a, b , c = 2, "hello"
print(a)  #not enough value to unpack
print(b)
print(c)

a = 2
b = 4
print(a)  # 4
print(b)  # print(a)
print(b)
print(c)