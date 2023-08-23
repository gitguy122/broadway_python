# Functions are the block of codes that are re-usable.
# If the same lines of code is repeated at multiple places in the code , then we can define a function
# for that code block and call wherever necessary

# There are things we need to keep in mind while creating a function:
# 1. Function Definition
# 2. Function  Call

# let's create a simple function whether a number is odd or even

def is_even(number):  # This is a function definition
    if number % 2 == 0:
        return True
    else:
        return False

result = is_even(43)  # Function call
print(result)