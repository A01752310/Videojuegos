"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

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
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    # Levanta el lápiz para que no dibuje mientras se mueve a la posición inicial
    up()
    goto(start.x, start.y)
    down()  # Baja el lápiz para comenzar a dibujar

    begin_fill()  # Inicia el llenado del rectángulo

    # Dibuja los lados del rectángulo
    for _ in range(2):
        # Avanza la distancia horizontal entre los puntos start y end
        forward(end.x - start.x)
        left(90)  # Gira a la izquierda 90 grados para dibujar el lado vertical
        # Avanza la distancia vertical entre los puntos start y end
        forward(end.y - start.y)
        left(90)  # Gira a la izquierda 90 grados para dibujar el lado horizontal

    end_fill()  # Finaliza el llenado del rectángulo

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
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
