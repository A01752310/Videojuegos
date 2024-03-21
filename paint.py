"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
import math
from turtle import * #Importa todas las funciones de la librería turtle

from freegames import vector #Importa la clase vector de la librería freegames

#Las siguientes funciones dibujan diferentes formas geometricas
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    r = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    
    pen = Turtle()
    pen.hideturtle()  
    pen.up()
    pen.goto(start.x, start.y - r)  # Ajusta la posición para el centro del círculo
    pen.down()
    pen.circle(r)


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO

# Maneja los clics en la pantalla, guardando el punto de inicio o dibujando la forma que se seleccionó
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

# Almacena una variable para cambiar las formas a dibujar
def store(key, value):
    """Store value in state at key."""
    state[key] = value

# Es el estado inicial del programa, determinando el punto donde inicia y la forma actual a dibujar
state = {'start': None, 'shape': line}

# Es la configuración inicial de la ventana de Turtle
# Tambien detecta las teclas presionadas por el usuario
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
#Color nuevo 
onkey(lambda: color('purple'),'P')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
