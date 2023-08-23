# creating a temporary variable 'temp'

a = 2
b = 4
print(a)  # 4
print(b)  # print(a)

temp = a
a = b
b = temp
print(a)
print(b)

a = 1
b = 2
a, b = b, a
print(a)  # 2
print(b)  # 1
