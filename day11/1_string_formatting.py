# We can format string using f-strings
name = input("Enter your name")
age = int(input("enter your age"))
language = input("Enter the language you are learning")
message = f"Hello I am {name}.I am learning {language}"
print(message)


message = 'I am %s and i am %d years old' % (name, age)
print(message)

message = f"I am {name} and I am {age}years old"
print(message)

#### Using format()  method  ####
message = "I am {} and I am {} years old.".format(name, age)
print(message)

message = 'I have {1}, {0}, and {2} in my bag'.format('book', 'pen', 'coffee')
print(message)


message = 'I have {1}, {0}, and {} in my bag'.format('book', 'pen')  # it raises error if the some format

print(message)

