from turtle import Screen
from paddles import Paddles
from pelota import Ball

#* Configuración de la Pantalla 
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title('Pong Game')
screen.tracer(0)

#* Inicialización de los paddles
paddle1 = Paddles(285,0)
paddle2 = Paddles(-285,0)

#* Inicializamos la pelota
ball = Ball()

#* Configuración del movimiento de los paddles
screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

band = True
while band:
    #* Visualizamos pantalla
    screen.update()

    #* Movimiento de la pelota
    ball.movement
    #? Choque con los limites de la pantalla
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.luffyg4
    #? Choque con los paddles
    if ball.distance(paddle1) < 30 or ball.distance(paddle2) < 30 :
        ball.luffyg4x
        


screen.exitonclick()