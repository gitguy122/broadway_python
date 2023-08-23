# Create a class Circle with an attribute radius. Create two objects of circle c1 and c2.Add the radius of the circles
# and print the result.
# Do the above task using a method and then a magic method
# Compare the size of the circle and print the result using magic method

class Circle:
    def __int__(self, radius,):
        self.radius = radius

    def add_radius(self, obj2):
        return self.radius + obj2.radius

    c1 = Circle(3)
    c2 = Circle(4)
    result = c1.radius + c2.radius
    print(result)

    result = c1.add_radius(c2)
        return f" Circle has {self.radius} radius and {self.length} length"

obj = Circle()
print(obj.radius())