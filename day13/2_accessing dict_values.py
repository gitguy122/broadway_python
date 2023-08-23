vowels = ["a", "e", "i", "o", "u"]
print(vowels[4])  # u


# Accessing dictionary is similar to that of accessing list elements
student = {"name": "john", "age": 25, "department": "CS"}
dept = student["department"]
print(dept)

name = student["name"]
print(name)  # john

# print(student["dob"]  # This raises keyerrror


# Accessing values using get() method
department = student.get("age")
print(department)  # 25
dob = student.get("dob")
print(dob)  # None



# Adding key-value pair in a dictionary
student = {"name": "john", "age": 25, "department": "CS"}
student["dob"] = "22 july"
print(student)  # {'name': 'john', 'age': 25, 'department': 'CS', 'dob': '22 july'}

student.update(roll_no=12)
print(student)  # {'name': 'john', 'age': 25, 'department': 'CS', 'dob': '22 july', 'roll_no': 12}

student["name"] = "jane"
print(student)  # {'name': 'jane', 'age': 25, 'department': 'CS', 'dob': '22 july', 'roll_no': 12}

# Removing a key-value pair from a dictionary
student = {'name': 'jane', 'age': 25, 'department': 'CS', 'dob': '22 july', 'roll_no': 12}
result = student.pop("dob")
print(result)  # 22 july
print(student)  # {'name': 'jane', 'age': 25, 'department': 'CS', 'roll_no': 12}

result = student.popitem()
print(result)  # ('roll_no', 12)

student.clear()
print(student)  # {}

del student