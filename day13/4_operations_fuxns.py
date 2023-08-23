student = {"name": "john", "age": 25, "department": "CS"}
print("name" in student)  # True
print("john" in student)  # False


# Built-in functions
print(len(student))  # 3

result = sorted(student)
print(result)  # ['age', 'department', 'name']

print(str(student))  # {'name': 'john', 'age': 25, 'department': 'CS'}