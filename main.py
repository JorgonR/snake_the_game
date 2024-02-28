from food import Food
from snake import Snake
from scoreboard import Scoreboard
from time import sleep
from turtle import Screen

SLEEP = 0
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

xcord = snake.lead.xcor()
ycord = snake.lead.ycor()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
  screen.update()
  sleep(SLEEP)
  snake.move()
  #Food Capture Check
  if snake.lead.distance(food) < DISTANCE:
    scoreboard.score += 1
    scoreboard.change_score()
    food.refresh()
    snake.add_to_snake(
      snake.block_chain[-1].xcor(),
      snake.block_chain[-1].ycor()
    )
  #Wall Collision Check
  if abs(xcord) > 280 or abs(ycord) > 280:
    print("wall")
    game_on = False
    scoreboard.game_over()
  #Tail Collision Check
  for block in snake.block_chain[1:]:
    print(block.xcor(), block.ycor())
    if snake.lead.distance(block) < DISTANCE:
      print("tail")
      game_on = False
      scoreboard.game_over()
  


screen.exitonclick()