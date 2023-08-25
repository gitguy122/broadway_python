# Create a dictionary students with keys id, name, age, department. Take a input from the user, which info
# (id, name, age or department) he wants to access and print the result. Handle the possible exceptions

student = {"name": "ram", "age": 1, "department": "math"}
try:
    key = input("enter the key you want to acccess")
    data = student[key]
    print(f"The {key} of the student is {data}")
except KeyError:
    print("please enter a valid key")


