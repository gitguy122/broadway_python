# Operator overloading is the way of defining how an operator behaves in it's operation
# For example '+' operator in the integer operation behaves different than in the string operation

a = 1
b = 2
print(a + b)  # 3

m1 = "Hello World"
m2 = "i am fine"
print(m1 + m2)  # "Hello Worldi am fine"

# Such operator functions are defined in the built-in classes of Python. These  methods are called
# magic methods. __add(), __mul(), __gt(), __lt(), __sub() etc.are the examples of magic methods

a = 2
b = 3
print(a + b)  # 3
print(a.__add__(b))  # 3