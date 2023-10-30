import turtle
wd=turtle.Screen()
shp=turtle.Turtle()
shapes=input("How many side")
shapes=int(shapes)
num=(360/shapes)
for i in range(shapes):
    shp.forward(100)
    shp.left(num)
