from turtle import Screen
from paddle import Paddle
from  ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # turn off the animation , we can't see any shape on screen , it will be turns on with paddle.update() code

r_paddle = Paddle(350)
l_paddle=Paddle(-350)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on=True
while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #Detect collision with wall
  if ball.ycor()>280 or ball.ycor()<-280:
      ball.bounce_y() #when the ball collision with up wall it have to return

  #Detect collision with paddles
  if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320) :
      ball.bounce_x()

  #Detect right paddle misses:
  if ball.xcor()>380:
      ball.reset_position()
      scoreboard.l_point()
      scoreboard.update_scoreboard()

      # Detect left paddle misses:
  if ball.xcor() < -380:
      ball.reset_position()
      scoreboard.r_point()
      scoreboard.update_scoreboard()


screen.exitonclick()