from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.goto(0,0)
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1 #define the speed of ball

    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def bounce_y(self):
        self.y_move *= -1 #reverse the direction of y movement when it goes to up

    def bounce_x(self):
        self.x_move *= -1 #reverse the direction of y movement when it goes to up
        self.move_speed *= 0.9 #speed up the ball movement

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

