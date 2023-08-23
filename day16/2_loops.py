# loops are used to run the certain block of codes repeatedly
# these are used to reduce the manual effort and perform the task in automated way
# there are two types  of loops in python; for loop and while loop

# for loop in different datatypes
vowels = ["a", "e", "i", "o", "u"]

for each in vowels:
    print(vowels)

# looping is similar in tuple, list and set

# Now lets see looping in Dictionary Type
student = {"name": "jon", "age":25, "address": "KTM"}
print(student.keys())

for key in student.keys():
    print(key)

print(student.values())
for value in student.values():
    print(value)
print(student.items())

for key, value in student.items():
    print(key)
    print(value)

# range() function
# we can give three parameters n the range function range(start, end, step_size)

a = range(10)  # gives from 0 to 9 ; 10 is exclusive
print(a)
print(list(a))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = range(2, 10)  # gives from 2 to 9
print(list(a))  # [2, 3, 4, 5, 6, 7, 8, 9]

a = range(2, 10, 2)
print(list(a))  # [2, 4, 6, 8]

squared = []
for i in range(1, 13):
    squared.append(i**2)
print(squared)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]

squared = [i**2 for i in range(1, 13)]  # list comprehension
print(squared)


###### enumerate() ######
# enumerate() function can take 2 parameters, iterable/ sequence and start value

vowels = ["a", "e", "i", "o", "u"]
print(enumerate(vowels))  # enumerate object
print(list(enumerate(vowels)))

for index, loop in enumerate(vowels):
    print(index)
    print(value)

for index, loop in enumerate(vowels, start=1):
    print(index)
    print(value)