from turtle import Screen
from paddles import Paddles

#* Configuración de la Pantalla 
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title('Pong Game')
screen.tracer(0)

#* Inicialización de los paddles
paddle1 = Paddles(285,0)
paddle2 = Paddles(-285,0)

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


screen.exitonclick()