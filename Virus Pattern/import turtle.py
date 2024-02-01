import turtle

screen = turtle.Screen()
screen_width = screen.window_width()
screen_height = screen.window_height()

screen.setup(width = screen_width, height= screen_height)
screen.bgcolor("black") #background color

turtle.speed(30) #set the lower speed for smoother movement 
turtle.color('red')
turtle.delay(2) #add a delay of 2 miliseconds

b = 200
while b> 0:
    turtle.left(b)
    turtle.forward(b * 3)
    b = b -1

turtle.done()    
