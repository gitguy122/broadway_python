# Function / Method Overloading
# If the Function is defined inside a class then the function is called a method.Method are called
# using object


# Function overloading is a term used in the Python if the same function definition is repeated multiple times.
# Python doesn't support function overloading or method overloading.


def addition(a, b):
    return a + b

def addition(a, b, c):
    return


r2 = addition(2, 3, 4)
print(r2)

# Even if we have defined two addition funcitons with different number  of parameters, but  the latest one is
# only considered in Python.

# This problem in Python can be solved in a tricky way

def addition(a, b, c=0, **kwargs):
    return a + b + c + sum(kwargs.values())

r1 = addition(2, 3)
r2 = addition(2, 3, 4, p=2, q=3)
print(r1)  # 5
print(r2)  # 14


class A:
    def test_fxn(self):
        return "I'm learning Python"

    def text_fxn(self):
        return "Hello World"

obj = A()
print(obj.text_fxn())

# Like function overloading, method overloading is also not possible in Python
