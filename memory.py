"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *
from freegames import path

# Carga la imagen del coche
car = path('car.gif')
tiles = list(range(32)) * 2     # Crea una lista de números para representar las fichas
state = {'mark': None}          # Estado del juego (marca de la ficha seleccionada)
hide = [True] * 64              # Lista para ocultar las fichas
tap_count = 0                   # Contador de taps
    
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def check_game_over():
    """Check if all tiles are uncovered."""
    if all(not hide[count] for count in range(64)):
        print("¡Felicidades! Has destapado todos los cuadros.")

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        tap_count += 1  # Incrementa el contador de taps

    update_tap_count()
    check_game_over()  # Verifica si todos los cuadros están destapados

def update_tap_count():
    """Update tap count displayed on the screen."""
    up()
    goto(-200, 200)
    down ()
    color('black')
    write(f'Taps: {tap_count}', font=('Arial', 16, 'normal'))

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update_tap_count()
    update()
    ontimer(draw, 100)

# Baraja las fichas
shuffle(tiles)

# Configuración inicial de la ventana y controles
setup(420, 420, 370, 0)
addshape(car)   # Carga la imagen del coche
hideturtle()
tracer(False)
onscreenclick(tap)  # Responde al clic en la pantalla
draw()  # Inicia el bucle principal del juego
done()  # Finaliza la ejecución del programa
