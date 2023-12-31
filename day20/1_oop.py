# OOP stands for Object-Oriented Programming
# It is the way of the modelling the real world problems into a program
# IT has  two important components; Class and the Objects

# Classes are the blueprints of object
# Objects are the instances of the class


class Vehicle:
    category = "car"  # This is a class attribute

v = Vehicle()  # This is creating an object of class Vehicle
print(v.category)  # car  # This is getting class attribute using an  object
print(Vehicle.category)  #car  # This is getting class attribute  using a class

v.category = "truck"
print(Vehicle.category)  # car
print(v.category)  # truck

class Vehicle:
    category = "car"  # class attribute

    def __init__(self, doors, color):  # this is a constructor
        self.doors = doors  # instance attribute
        self.color = color  # instance attribute

    def description(self):
        return f"Vehicle is {self.category}.Color is {self.color} and doors are {self.doors}"

    def change_color(self, color):
        self.color = "blue"

v1 = Vehicle(4, "red" )
print(v1.category)  # car  # get data
print(v1.doors)  # 4
print(v1.color)  # red

v1.category = "bike"  #  set data
print(Vehicle.category)  # car  # get_data
print(v1.category)  # bike  # get_data

v2 = Vehicle(2, "green")
print(v2.doors)  # 2
print(v2.color)  # green
print(v2.description())
print(v2.color)



# function inside a class is called the method of that class and that can be called with
# object of the class only