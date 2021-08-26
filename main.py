'''
This is a python program utilizing the turtle library

This program draws the classic python logo with the python turtle library
'''
import turtle # Import the Python2.5+ turtle library
import time # Import the time library for time.sleep()

blue = turtle.Turtle() # Define "blue" as a turtle
yellow = turtle.Turtle() # Define "yellow" as a turtle

blue.color('#4682B4') # Set blue's color to "Cornflower Blue" AKA #4682B4
yellow.color('#FFD700') # Set yellow's color to "Gold" AKA #FFD700

def drawBlue(): # Define a function to draw "blue"
  blue.penup() # "Hold" the "pen" up so it will not draw
  blue.goto(-40, 115) # Makes blue go to the coordinates (-40, 115)
  blue.pendown() # "Hold" the "pen" down so it will draw
  blue.begin_fill() # Begin the filling cycle
  blue.left(20) # Turn left 20 degrees
  for i in range(20): # Repeat the below code 20 times
    blue.right(2) # Turn right 2 degrees
    blue.forward(5) # Move forward 5 degrees
  blue.right(71) # Turn right 71 degrees
  blue.forward(100) # Move forward 100 pixels
  blue.right(23) # Turn right 23 degrees
  blue.forward(5) # Move forward 5 pixels
  blue.right(22) # Turn right 22 degrees
  blue.forward(5) # Move forward 5 pixels
  blue.right(22) # Turn right 22 degrees
  blue.forward(5) # Move forward 5 pixels
  blue.right(23) # Turn right 23 pixels
  blue.forward(100) # Move forward 100 pixels
  blue.left(23) #  Turn left 23 pixels
  blue.forward(5) # Move forward 5 pixels
  blue.left(22) # Turn left 22 degrees
  blue.forward(5) # Move forward 5 pixels
  blue.left(22) # Turn left 22 degrees
  blue.forward(5) # Move forward 5 pixels
  blue.left(23) # Turn left 23 degrees
  blue.forward(50) # Move forward 50 pixels
  blue.right(90) # Turn right 90 degrees
  blue.forward(35) # Move forward 35 pixels
  blue.right(65) # Turn right 65 degrees
  for i in range(22): # Repeat below code 22 times
    blue.right(2) # Turn right 2 pixels
    blue.forward(5) # Move forward 5 pixels
  blue.right(71) # Turn right 71 degrees
  blue.forward(100) # Move forward 100 pixels
  blue.left(90) # Turn left 90 degrees
  blue.forward(15) # Move forward 15 pixels
  blue.left(90) # Turn left 90 degrees
  blue.forward(40) # Move forward 40 pixels
  blue.right(90) # Turn right 90 degrees
  blue.forward(48) # Move forward 48 pixels
  blue.end_fill() # End the filling cycle
  blue.penup() # "Hold" the "pen" up so it will not draw
  blue.hideturtle() # Hide the blue triangle
  
def drawYellow(): # Define a function to draw "yellow"
  yellow.penup() # "Hold" the "pen" up so it will not draw
  yellow.goto(40, -115) # Makes yellow go to the coordinates (40, -115)
  yellow.pendown() # "Hold" the "pen" down so it will draw
  yellow.begin_fill() # Begin the filling cycle
  yellow.right(-20) # Turn right -20 degrees
  for i in range(20): # Repeat below code 20 times
    yellow.left(-2) # Turn left -2 degrees
    yellow.forward(-5) # Move forward -5 pixels
  yellow.left(-71) # Turn left -71 degrees
  yellow.forward(-100) # Move forward -100 pixels
  yellow.left(-23) # Turn left -23 degrees
  yellow.forward(-5) # Move forward -5 pixels
  yellow.left(-22) # Turn left -22 degrees
  yellow.forward(-5) # Move forward -5 pixels
  yellow.left(-22) # Turn left -22 degrees
  yellow.forward(-5) # Move forward -5 pixels
  yellow.left(-23) # Turn left -23 degrees
  yellow.forward(-100) # Move forward -100 pixels
  yellow.right(-23) # Turn right -23 degrees
  yellow.forward(-5) # Move forward -5 pixels
  yellow.right(-22) # Turn right -22 degrees
  yellow.forward(-5) # Move forward -5 pixels
  yellow.right(-22) # Turn right -22 degrees
  yellow.forward(-5) # Move forward -5 pixels
  yellow.right(-23) # Turn right -23 degrees
  yellow.forward(-50) # Move forward -50 pixels
  yellow.left(-90) # Turn left -90 degrees
  yellow.forward(-35) # Move forward -35 pixels
  yellow.left(-65) # Turn left -65 degrees
  for i in range(22): # Repeat below code 22 times
    yellow.left(-2) # Turn left -2 degrees
    yellow.forward(-5) # Move forward -5 pixels
  yellow.left(-71) # Turn left -71 degrees
  yellow.forward(-100) # Move forward -100 degrees
  yellow.right(-90) # Turn right -90 degrees
  yellow.forward(-15) # Move forward -15 degrees 
  yellow.right(-90) # Turn right -90 degrees
  yellow.forward(-40) # Move forward -40 pixels
  yellow.left(-90) # Turn left -90 degrees
  yellow.forward(-48) # Move forward -48 pixels
  yellow.end_fill() # End the filling cycle
  yellow.penup() # "Hold" the "pen" up so it will not draw
  yellow.hideturtle() # Hide the yellow triangle

def drawEyes():
  blue.color('white') # Sets blue's color to "white"
  blue.goto(-18, 100) # Makes blue go to coordinates (-18, 100)
  blue.pendown() # "Hole" the "pen" down
  blue.begin_fill() # Begin the filling cycle
  blue.circle(7) # Draw a circle with a radius of 7 pixels
  blue.end_fill() # End the filling cycle
  yellow.color('white') # Sets yellow's color to "white"
  yellow.goto(30, -100) # Makes yellow go to coordinates (30, -100)
  yellow.pendown() # "Hold" the "pen" down
  yellow.begin_fill() # Begin the filling cycle
  yellow.circle(7) # Draw a circle with a radius of 7 pixels
  yellow.end_fill() # End the filling cycle


def screenSetup(): # Define a function to setup the virtual screen
  screen = turtle.Screen() # Define "screen"
  screen.setup(width=.75, height=0.5, startx=None, starty=None) # Setup the screen with a width of 0.75 of the host's resolution width, and 0.50 of the host's resolution height
  screen.title("CSP Python Art") # Set the window title to "CSP Python Art"

# The "main" statement

screenSetup() # Run the screenSetup() function
start_time = time.time() # Start counting time
drawBlue() # Run the drawBlue() function
drawYellow() # Run the drawYellow() function
drawEyes() # Run the drawEyes() function
print("--- Took %s seconds to execute the program ---" % (time.time() - start_time)) # Print the execution time in the terminal
time.sleep(10) # Pause program execution for 10 seconds
