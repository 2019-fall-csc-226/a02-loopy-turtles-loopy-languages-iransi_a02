import turtle

wn = turtle.Screen()
bert = turtle.Turtle()
bert.speed(10)
bert.shape('turtle')
bert.color('purple', 'yellow')
bert.position()
(10.00,0.00)
bert.begin_fill()



for i in range(36):
    bert.forward(260)
    bert.left(190)

bert.end_fill()
head =16
pen = 10

bert.penup()
bert.forward(130)
bert.right(90)
bert.forward(90)
bert.pendown()
bert.color('green')

bert.forward(160)
bert.left(280)
bert.circle(-50, 100)
bert.right(150)

bert.circle(200, 140)
turtle.done()

