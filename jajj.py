import turtle                   # allows us to use the turtles library

wn = turtle.Screen()            # creates a graphics window
bert = turtle.Turtle()     # create a turtle named myturtle

bert.shape('square')       # shapes possible are 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
bert.color('red')

head = 0                        # initial heading for my_turtle
pen = 5                         # initial pensize for my_turtle
bert.forward(160)
bert.left(280)
bert.circle(-50, 100)
bert.right(150)

bert.circle(-300, 93)
wn.exitonclick()                # Added by Dr. Pearce. Closes the program when a user clicks in the window
