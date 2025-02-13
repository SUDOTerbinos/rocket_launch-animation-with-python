import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rocket Launch")

rocket = turtle.Turtle()
rocket.shape("square")
rocket.color("white")
rocket.shapesize(stretch_wid=5, stretch_len=2)
rocket.penup()
rocket.goto(0, -200)

fire = turtle.Turtle()
fire.shape("triangle")
fire.color("orange")
fire.shapesize(stretch_wid=2, stretch_len=1)
fire.penup()
fire.goto(0, -250)

def create_stars():
    star = turtle.Turtle()
    star.color("white")
    star.penup()
    star.speed(0)
    star.hideturtle()

    for _ in range(50):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        star.goto(x, y)
        star.dot(2)

def launch_rocket():
    fire_speed = 10
    for _ in range(40):  
        fire.showturtle()
        fire.goto(rocket.xcor(), rocket.ycor() - 30)
        time.sleep(0.05)  # Delay for smooth animation
        fire.hideturtle()
        
        rocket.sety(rocket.ycor() + 10)

import random
create_stars()

launch_rocket()

rocket.goto(0, 200)
rocket.write("Liftoff!", align="center", font=("Arial", 16, "bold"))

screen.mainloop()
