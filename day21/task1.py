# Create a class person with instance attributes name and age. create a method get_details in
# this class


class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name is {self.name} and age is {self.age}"

class Employee(Person):
    def __int__(self, name, age, salary, designation):
        super().__int__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):
        print(super().get_details())
        return f"salary is {self.salary} and designation is {self.designation}"

employee = Employee("jon", 30, 20000, "IT Officer")
print(employee.get_details())