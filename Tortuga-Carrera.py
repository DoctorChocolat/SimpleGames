from turtle import Turtle, Screen
import random

is_race_on= False

screen = Screen ()
screen.title("Carrera de Tortugas")
screen.screensize(500,400)
screen.bgcolor("green")
user_apuesta= screen.textinput(title="Que tortuga ganará", prompt="Elige un color")
colors = ["red", "yellow", "blue", "white", "orange", "black"]
y_position = [-150, -90, -30, 30, 90, 150]
all_turtles = []

#Six turtles with diferent colors, in one position each.
for total_index in range(0,6):

    new_turtle = Turtle()
    new_turtle.penup()
    #new_turtle.speed("fastest") if you want to improve the speed
    new_turtle.shape("turtle")
    new_turtle.shapesize(3, 2, 1)
    new_turtle.color(colors[total_index])
    new_turtle.goto(x=-400, y= y_position[total_index])
    all_turtles.append(new_turtle)

if user_apuesta:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 430:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_apuesta:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()