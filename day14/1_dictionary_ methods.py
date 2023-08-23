# copy()
student = {"name": "Jon", "age": 25}
student2 = student.copy()
print(student2)  #{'name': 'Jon', 'age': 25}
print(student)  # {'name': 'Jon', 'age': 25}

# get()
student = {"name": "Jon", "age": 25}
name = student.get("name")
print(name)  # jon
roll = student.get("roll")
print(roll)  # None
roll = student.get("roll", 1)
print(roll)  # 1
name = student.get("name", "ram")
print(name)  # jon

student = {"name": "Jon", "age": 25}
print(student.items())

# keys()
student = {"name": "Jon", "age": 25}
print(student.values())

# pop()
student = {"name": "Jon", "age": 25}
age = student.pop("age")
print(student)  # {'name': 'Jon'}

# popitem()
student = {"name": "Jon", "age": 25}
result = student.popitem()
print(result)  # {"age": 25}
print(student)  # {"name": "Jon"}

# update()
student = {"name": "Jon", "age": 25}
student.update(address="ktm")
print(student)  # {'name': 'Jon', 'age': 25, 'address': 'ktm'}

# fromkeys()
a = dict()
result = a.fromkeys([1, 2], "a")
print(result)  # {1: "a", 2: "a"}

# setdefault()
student = {'name': 'Jon', 'age': 25, 'address': 'ktm'}
student.setdefault("name", "Jane")
print(student)

student.setdefault("job", "overseer")
print(student)  # {'name': 'Jon', 'age': 25, 'address': 'ktm', 'job': 'overseer'}

