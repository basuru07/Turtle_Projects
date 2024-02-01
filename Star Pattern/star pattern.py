import turtle

screen = turtle.Screen()
screen_width = screen.window_width()
screen_height = screen.window_height()

screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black") #background color

turtle.speed(10)  #set the speed

#function to the draw a star pattern
def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

#draw a multiple star patterns
size = 100
for _ in range(36):
        turtle.color('yellow')
        draw_star(size)
        turtle.right(10)  
            
turtle.done()          
