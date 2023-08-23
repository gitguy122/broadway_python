# map()
# map is a built-in function that takes two parameters as an input.First parameter is function
# and second parameter is an iterable.
# map() function changes every elements n an iterable to some other form

nums = [1, 2, 3, 4, 5]
def increase_by_10(data):
    return data + 10

result = map(increase_by_10, nums)
print(nums)
print(list(result))

nums = [1, 2, 3, 4, 5]
def get_cubed_data(data):
    return data ** 3

result = map(get_cubed_data, nums)
print(list(result))