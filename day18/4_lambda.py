# lambda in python are the elegant to create a on-line functions
# These functions do not have name. So. they are also called as anonymous function


def addition(a, b):
    return a + b

summ = lambda a, b: a + b
print(summ(4, 5))

is_even = lambda x: x % 2 == 0
print(is_even(5))

nums = [1, 2, 3, 4, 5]

result = map(lambda x: x + 10, nums)
print(list(result))

nums = [1, 2, 3, 4, 5]
result = map(lambda x: x ** 3, nums)
print(list(result))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x % 5 == 0, nums)
print(list(result))

nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, nums)
print(result)

nums = [1, 2, 3, 4, 5]
result = map(lambda x: x % 5 == 0, nums)
print(list(result))