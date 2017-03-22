from myFunction import*
#brings and follows instructions from the function file
import turtle
#brings in turtle to draw shapes and designs
bob=turtle.Turtle()
#name of this turtle that draws a specific design
popo=turtle.Turtle()
#name of this turtle that draws a specific design
vegeta=turtle.Turtle()
#name of this turtle that draws specific design
popo.left(45)
#Is the angle of the design that this turtle is going to draw
vegeta.right(90)
#Is the angle of the design that his turtle is going to draw

bob.speed(0)
#Is how fast the turtle is going to draw its the design
popo.speed(0)
#Is how fast the turtle is going to draw its design
vegeta.speed(0)
#Is how fast the turtle is going to draw its design
turtle.bgcolor("cyan")
#bgcolor("cyan") changes the color of the bacground
turtle.colormode(255)
#colormode allows the shapes to be filled in with watever color you want

for times in range(255):
#This makes the loop of the repeated shapes.
    c=(times,34,45)
#This is the color sequence that gives the shapes their colors
    bob.color(c)
#bob.color(c) it tells the specific turtle what his color sequnce is.
    polygon(bob,7,40)
#this tells the turtle what shape it has to draw.
    bob.right(45)
#this tells the turtle what angle it has to draw the shapes
    bob.forward(times)
#this tells the turtle how much it has to move forward
    c=(times,65,23)
#This tells the color sequnce that gives the shapes their color
    popo.color(c)
#This tells popo his specific color sequnce.
    polygon(popo,5,60)
#This tells popo what shapes it needs to draw.
    popo.right(32)
#this tells the turtle what angle it needs to be drawn
    popo.forward(times)
#this tells the turtle how much it needs to move forward
    c=(times,74,80)
#this is the color sequence that gives the shapes its color
    vegeta.color(c)
#This tells its specific color sequence
    polygon(vegeta,5,20)
#This tells the turtle what shapes it needs to draw
    vegeta.left(60)
#This tells the turtle what angle it needs to draw
    vegeta.forward(times)
#this tells the turtle how much it nedds to move forward
    
