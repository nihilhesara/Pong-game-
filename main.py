from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)                    # To remove the animations

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()                 # Update screen after animation removed


screen.exitonclick() 