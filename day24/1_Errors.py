# Python the errors can be broadly classified into two sections:
# 1. Syntactic Error
# 2. Non-Syntactic Error


# Syntactic Error
# This type of error occurs when you mess up with the grammar of the language
# For example: making typo in keywords, messing up with indentations, whitespaces at unwanted places.

 a = 1  # Syntax error because of a whitespace in the beginning
# fo i in range(10):  # Syntax error because  of the typo in keyword
#     pass
# a = 5
# if a:
# print("hello world")  # Indentation Error


# Non-Syntactic Error
# These are all the errors except syntax error. They can further be classified in the followings:
# 1. TypeError
# 2. ValueError
# 3. ZeroDivisionError
# 4. keyError
# 5. AttributeError
# 6. IndexError
# 7. NameError
# 8. ModuleNotFoundError


# TypeError
# IT is raised when operations in different datatypes are performed which is not acceptable
# for example: 2 + "Hello World" . Int and String can't be operated with '+' operator


# ValueError
# It is raised if we try to convert a datatype to other datatype which is not possible
# For example: int("hello"). This raises Value Error


# ZeroDivision Error
# It is raised when we try to divide an object with 0
# print(3/0)  # ZeroDivision Error

# Attribute Error
# It is raised if an object tries to get an attribute which is not present in that object
# example: if a list object tries to excess the join() method. Join () is actually a  method in string.
# a = [1, 2 , 3]
# a.join("")  # Attribute Error

# KeyError
student = {"name": "Jon", "address": "KTM"}
print(student["phone"])  # KeyError because phone is not present in the dictionary


# IndexError
data = [1, 2, 3, 4]
print(data[10])  # IndexError

# NameError
# a = 1
# print(b)  # NameError: 'b' is not defined

# ModuleNotFoundError
# import mat  # ModuleNotFoundError because 'mat' is not a valid package