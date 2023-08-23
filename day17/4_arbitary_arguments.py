# *args and **kwargs  are the arbitary arguments
# These arguments can take dynamic number of parameter
# They are like an expandable bucket

def addition(*args):
    print(args)
    print(type(args))  # tuple
    return sum(args)

result = addition(1, 2, 3)
print(result)

def addition(**kwargs):
    print(kwargs)  # {"a": 1, "b": 2, "c": 3}
    print(type(kwargs))
    return sum(kwargs.values())
    
result = addition(a=1, b=2, c=3)
print(result)