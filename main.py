from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("SNAKE")
screen.tracer(0)

my_score = Scoreboard()
my_snake = Snake()
my_food = Food()


screen.listen()
screen.onkey(my_snake.go_right, "Right")
screen.onkey(my_snake.go_left, "Left")
screen.onkey(my_snake.go_up, "Up")
screen.onkey(my_snake.go_down, "Down")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.get_bigger()
        my_score.increase_score()

    if (my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290
            or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290):
        my_score.reset_game()
        my_snake.restart()

    for seg in my_snake.segments[1:]:
        if my_snake.head.distance(seg) < 10:

            my_score.reset_game()
            my_snake.restart()

    my_snake.move()

screen.exitonclick()
