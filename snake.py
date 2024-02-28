from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-30, 0), (-60, 0)]
SPEED = 1
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.block_chain = []
    for tup in STARTING_POSITIONS:
      self.add_to_snake(tup[0], tup[1])
    self.lead = self.block_chain[0]
  
  def add_to_snake(self, x_cor, y_cor):
    block = Turtle(shape="square")
    block.color("white")
    block.penup()
    block.goto(x_cor, y_cor)
    self.block_chain.append(block)

  def move(self):
    for idx in range(len(self.block_chain) - 1, 0, -1):
      x = self.block_chain[idx - 1].xcor()
      y = self.block_chain[idx - 1].ycor()
      self.block_chain[idx].goto(x, y)
    self.lead.forward(SPEED)

  def up(self):
    if self.lead.heading != DOWN:
      self.lead.setheading(UP)

  def down(self):
    if self.lead.heading != UP:
      self.lead.setheading(DOWN)

  def left(self):
    if self.lead.heading != RIGHT:
      self.lead.setheading(LEFT)

  def right(self):
    if self.lead.heading != LEFT:
      self.lead.setheading(RIGHT)