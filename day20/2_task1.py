# create a class person with instance attributes name and age. Create a method get_details in this class  to print name and age

class Person:



    def __init__(self, name , age):
        self.name = name
        self.age = age

    def description(self):
        return f" Name is {self.name} and is currently {self.age} years old."

person = Person("Jon", 40)
print(person.description())