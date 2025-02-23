#Omarion Neal
#9/20/23

#import turtle
import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.title("Ex 6b Soccer Ball ojn15 ")

# Create a Turtle for the pentagon
pentagon_turtle = turtle.Turtle()
pentagon_turtle.speed(1)  # Set the drawing speed
pentagon_turtle.color("blue")  # Set pen color for the pentagon

# Create a Turtle for the hexagon
hexagon_turtle = turtle.Turtle()
hexagon_turtle.speed(1)  # Set the drawing speed
hexagon_turtle.color("red")  # Set pen color for the hexagon

# Define the number of sides for each shape
pentagon_sides = 5
hexagon_sides = 6

# Define the turn angles
pentagon_angle = 360 / pentagon_sides
hexagon_angle = 360 / hexagon_sides

# Draw the pentagon
for times in range(pentagon_sides):
    pentagon_turtle.forward(70)  # Adjust the length
    pentagon_turtle.left(pentagon_angle)

# Lift the pen and move to a new position for the hexagon
hexagon_turtle.penup()
hexagon_turtle.goto(180, 0)  # Adjust the position 
hexagon_turtle.pendown()

# Draw the hexagon
for times in range(hexagon_sides):
    hexagon_turtle.forward(90)  # Adjust the length 
    hexagon_turtle.left(hexagon_angle)

# Close the Turtle graphics window on click
screen.exitonclick()




