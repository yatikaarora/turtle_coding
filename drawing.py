#to draw an octagon and a nested loop within.
import turtle
turtle= turtle.Turtle()
sides = 8
for steps in range(sides):
     turtle.forward(100)
     turtle.right(360/sides)
     for moresteps in range(sides):
         turtle.forward(50)
         turtle.right(360/sides)
