import sys
# Import the library

import matplotlib.pyplot as plt


# Create a class Circle
class Circle(object):

    def __init__(self,color="blue",radius=2):
        self.color=color
        self.radius=radius

    def add_radius(self,r):
        self.radius=self.radius+r
        return self.radius

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0),self.radius,fc=self.color))
        plt.axis('scaled')
        plt.show()
# Create an object RedCircle

RedCircle = Circle('red',5)
## Find out the methods can be used on the object RedCircle with dir
print(dir(RedCircle))
print(RedCircle.radius)
print(RedCircle.color)
print(RedCircle.radius)
#to print call the function
RedCircle.drawCircle()
#-----------------------------------------------------------------------------
# Use method to change the object attribute radius

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)
#---------------------------------------------------------------------------
#"now blue circle"
BlueCricle=Circle(radius=100)#here it was already defined the color was set to blue
print(BlueCricle.color)
BlueCricle.drawCircle()
#---------------------------------------------------------------------------------
class Rectangle(object):

    def __init__(self,width=3,height=6,color="blue"):
        self.width=width
        self.height=height
        self.color=color

    def changeWidth(self,w):
        self.width=self.width+w
        return(self.width)

    def RentangleDraw(self):
        plt.gca().add_patch(plt.Rectangle((0,0),self.width,self.height,fc=self.color))
        plt.axis('scaled')
        plt.show()

WhiteRectange=Rectangle(color="white",height=9,width=10)
WhiteRectange.RentangleDraw()
SkinnyRenctangle=Rectangle(2,10,"blue")
SkinnyRenctangle.RentangleDraw()