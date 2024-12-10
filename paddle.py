from turtle import Turtle, Screen


class Paddle(Turtle):
   def __init__(self,x_position):
       super().__init__()
       # self.paddle = Turtle()
       self.shape(name="square")
       self.color("white")
       self.shapesize(stretch_wid=5,stretch_len=1)  # witdh and height in turtle  start from 20 so the shape with size of 20*100 turn to 1*5
       self.penup()
       self.goto(x_position, 0)

   # def create_paddle(self,x_position):


   def go_up(self):
       self.goto(self.xcor(),self.ycor()+20)

   def go_down(self):
       self.goto(self.xcor(), self.ycor() - 20)






