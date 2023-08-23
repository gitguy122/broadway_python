# decorators are the higher order function in python which adds extra function to the existing
# existing function

# if a function takes another function as a argument , then such a function  is called higher
# order function. map(), filer(), sorted(), all the decorators are higher order functions.


########  Closure ##########
# Closure is a concept in python which satisfies the following points
# 1. There should be a nested function i.e a function inside another function
# 2. Inner function must refer to the value of outer function
# 3. Outer funciton must return inner function

def outer_func(message):
    def inner_func():
        print(message)
    return inner_func

result = outer_func("hello world")
result()