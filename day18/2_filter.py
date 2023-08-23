# filter()
# filter() is a built-in function that takes two parameters as an input . First parameter is a function
# and second parameter is an iterable.
# filter() function filters the element from an iterable  and returns a new sequence
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_even_nums(data):
    return  data % 2 == 0

result = filter(get_even_nums, nums)
print(nums)
print(list(result))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def get_multiples_nums(data):
    return data % 5 == 0

result = filter(get_multiples_nums, nums)
print(nums)
print(list(result))
