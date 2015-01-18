import turtle

def draw_square(some_turtle):    
                for i in range(1,5):
                    some_turtle.forward(100)
                    some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("RED")

    #create object and function call to draw turtle
    brad = turtle.Turtle()
    for x in range(1,20):
        draw_square(brad)
        brad.right(10)
    
    #create object to do make a circle 
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()
    
draw_art()
