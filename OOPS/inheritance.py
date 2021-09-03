class Shape:                #parent class/base class/super class
    def drawRect(self):
        print("drawing rectangle...")
    def drawCirc(self):
        print("drawing circle...")
class Colour(Shape):            #child class/derived class/sub class
    def toColour(self):
        print("rectangle coloue : blue")
        print("circle colour : red")
s=Shape()
s.drawCirc()
s.drawRect()
print("-----------------------")
c=Colour()
c.drawCirc()
c.drawRect()
c.toColour()