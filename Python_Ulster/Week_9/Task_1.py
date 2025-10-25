import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
        print(f"The area of the circle in {self.area():.2f} and the circumference is {self.circumference():.2f}")
    def area(self):
        result = math.pi * (self.radius**2)
        return result
    def circumference(self):
        result = math.pi * 2 * self.radius
        return result

radius = int(input("Enter the radius for the circle: "))
user_circle = Circle(radius)
user_circle.__str__()
