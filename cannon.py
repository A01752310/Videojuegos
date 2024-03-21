"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *
from freegames import vector

# Inicialización de posición de la pelota y su velocidad
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []                # Lista que almacena los objetivos


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200
    # Comprobación dentro de los parametros    

def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')         # Dibuja los objetivos como puntos azules

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')           # Dibuja la pelota como un punto rojo

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)      # Agrega un nuevo objetivo aleatorio

    for target in targets:
        target.x -= 0.5             # Mueve los objetivos hacia la izquierda

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)            # Mueve la pelota según la velocidad actual

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)  # Elimina los objetivos que están demasiado cerca de la pelota

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

# Configuración inicial de la ventana y controles
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()  # Inicia el bucle principal del juego
done()  # Finaliza la ejecución del programa
