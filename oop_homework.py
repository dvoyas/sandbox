# # Object Oriented Programming
# ## Homework Assignment

import math


#
# #### Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2)

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())


print(li.slope())


# ________
# #### Problem 2

# Fill in the class 
class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * 3.14 * self.radius * self.height + 2 * 3.14 * self.radius ** 2


# EXAMPLE OUTPUT
c = Cylinder(2, 3)

print(c.volume())

print(c.surface_area())



