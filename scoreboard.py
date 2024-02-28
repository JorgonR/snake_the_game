from turtle import Turtle

ALIGNMENT = "center"
FONT = ("New Times Roman", 20, "normal")

class Scoreboard:
  def __init__(self):
    board = self.create_turtle()
    self.board = board
    self.score = 0
    self.change_score()
    
  def create_turtle(self):
    board = Turtle()
    board.color("white")
    board.penup()
    board.goto(0, 260)
    return board
    
  def change_score(self):
    self.board.clear()
    self.board.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    self.board.hideturtle()

  def game_over(self):
    self.board.goto(0, 0)
    self.board.write("GAME OVER", align=ALIGNMENT, font=FONT)
    