# Problem: Define a circle class to create a circle with radius r using the constusctor. Define an Aera() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

import math
class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius*self.radius

    def perimeter(self):
        return 2*math.pi*self.radius
    
c = circle(8)
print(c.area())
print(c.perimeter())