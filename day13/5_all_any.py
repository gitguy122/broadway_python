# all(iterable) built-in function
# all() fucntion takes an iterable /sequence as a parameter
# if all the elements of that iterable are truthy then It returns True

result = all([1, 2, "jon"])
print(result)  # True

result = all([0, "jane"])
print(result)  # False

# any(iterable) built-in function
# any() function takes an iterable / sequence  as a parameter
# if any one of the elements of that iterable is truthy then it returns True
print(any(["", {}, 1]))  # True
print(any([0, []]))  # False

# there is one exception
result = all([])
print(result)  # True
