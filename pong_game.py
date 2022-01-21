from turtle import Screen, Turtle
from paddles import Paddles
from pelota import Ball
from score import Score

def first_lines(line):
    """
    Esta función dibuja una linea punteada del centro de la pantalla
    hacia abajo hasta el limite de esta
    -------
    Args:
        line -> Recibe un objeto de la clase Turtle
    -------
    """
    line.stamp()
    line.forward(50)


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

#* Inicializamos el marcador
score = Score()

#* Configuración del movimiento de los paddles
screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

#* Linea del tablero
cont, line = 0, Turtle("square")
line.color('white')
line.right(90)
line.pu()
while cont <= 300:
    first_lines(line)
    cont += 50
line.home()
line.right(270)
cont = 0
while cont <= 300:
    first_lines(line)
    cont += 50

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
    
    #* Puntos
    if ball.xcor() > 300:
        ball.reset_ball
        score.points_paddle1
    
    if ball.xcor() < -300:
        ball.reset_ball
        score.points_paddle2
    
    if score.score_paddle1 >= 5:
        print('JUGADOR DE LA DERECHA ES EL GANADOR'.center(100,'='))
        band = False
    elif score.score_paddle2 >= 5:
        print('JUGADOR DE LA IZQUIERDA ES EL GANADOR'.center(100,'='))
        band = False

screen.exitonclick()
