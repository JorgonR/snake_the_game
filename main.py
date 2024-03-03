from food import Food
from snake import Snake
from scoreboard import Scoreboard
from time import sleep
from turtle import Screen

SLEEP = 0.2
DISTANCE = 15

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.change_score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
  lead_x = snake.lead.xcor()
  lead_y = snake.lead.ycor()
  screen.update()
  sleep(SLEEP)
  snake.move()
  #Food Capture Check
  if snake.lead.distance(food) < DISTANCE:
    scoreboard.score += 1
    scoreboard.change_score()
    food.refresh()
    snake.add_to_snake(
      snake.block_chain[-1].position()
    )
  #Wall Collision Check
  if abs(lead_x) > 280 or abs(lead_y) > 280:
    game_on = False
    scoreboard.game_over()
  #Tail Collision Check
  for block in snake.block_chain[1:]:
    if snake.lead.distance(block) < DISTANCE:
      game_on = False
      scoreboard.game_over()
  


screen.exitonclick()