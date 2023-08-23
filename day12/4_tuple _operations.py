# concatenation

a = (1, 2, 3)
b = (4, 5, 6)
result = a + b
print(result)  # (1, 2, 3, 4, 5, 6)

# Repetition /  broadcast(b)
a = (1, 2)
result = a * 3
print(result)

# membership operation ("in", and "not in")
print(2 in (1, 2, 3))
print(3 not in (1, 2, 3))

# Iteration
vowels = ("a", "e", "i", "o", "u")
for each in vowels:
    print(each)

data = [i**2 for i in range(10)]  # list comprehension
print(data)
data = (i**2 for i in range(10))
print(data)
