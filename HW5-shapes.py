#Shapes.py
#Python Homework
#WEIWEI SU
#U17420699
#Last modified Date: 10/26/2017

import math

class Point:
    """Models a point in the plane using Cartesian coordiantes, default is 0"""
    #initialize input value
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Output format Overloading
    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    #Point Movements (Will also count Center movement of Ellipse and Circles)
    #Note: if dx or dy's input value is Zero, then it means the point will not move on the selected axis.
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    #Distance between two points
    def dist(self, point):
        return round(math.sqrt(math.pow(point.x - self.x, 2) + math.pow(point.y - self.y, 2)), 1)


class Ellipse(Point):
    #initialize input value
    def __init__(self, center, x_extent, y_extent):
        self.x_extent = x_extent
        self.y_extent = y_extent
        Point.__init__(self, center.x, center.y)

    #Output format Overloading
    def __str__(self):
        return "Ellipse with Center: ({}, {}); Width: {}; Height: {}".format(self.x,self.y, self.y_extent*2, self.x_extent*2)

    #Calculate Ellipse Area
    def get_area():
        return round(math.pow(math.pi*self.x, 2) + math.pow(math.pi*self.y, 2) ,1)

    #Ellipse Center Movement
    def translate(self, dx, dy):
        return super().translate(dx, dy)

class Circle(Ellipse):

    def __init__(self, center, r):
        self.radius = r
        Point.__init__(self, center.x, center.y)
    
    #Output overloading
    def __str__(self):
        return "Circle with Center: ({}, {}); Radius: {}".format(self.x, self.y, self.radius)

    #Get area of the circle
    def get_circle_area(self):
        return round(math.pi*math.pow(self.radius, 2), 1)

    #Move a circle
    def translate(self, dx, dy):
        return super().translate(dx, dy)

    #Decide if one circle is inside another
    def contains(self,other):
        ''' returns True if and only if circle other is completely contained inside circle self'''
        #Calculate distance between the center of two circles
        distance = math.sqrt(math.pow(other.x - self.x,2) + math.pow(other.y - self.y,2))

        #Then compare
        if self.radius > (distance + other.radius):
            return True
        else:
            return False
        
        #Note to TA:
        #For this code when executing statement A.contain(B) it would be like: "if Circle B is inside Circle A"



#Prompt Enter values for Ellipse
def getEllipse():
    width = float(input("Enter Ellipse's Width"))
    height = float(input("Enter Ellipse's Height"))
    ctrPoint_x = float(input("Enter the x cooridinate for center point"))
    ctrPoint_y = float(input("Enter the y cooridinate for center point"))
    p = Point(ctrPoint_x,ctrPoint_y)
    return Ellipse(p, height, width)

#Prompt Enter values for Circle
def getCircle():
    radius = float(input("Enter Circle's radius"))
    ctrPoint_x = float(input("Enter the x cooridinate for center point"))
    ctrPoint_y = float(input("Enter the y cooridinate for center point"))
    p = Point(ctrPoint_x,ctrPoint_y)
    return Circle(p, radius)