"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import *
from turtle import *
from freegames import square, vector

# Creación de la comida y serpiente
food = vector(0, 0)         # Comida posicion inicial
snake = [vector(10, 0)]     # Serpiente inicialización
aim = vector(0, -10)        # Apuntar

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
    # Asigna dirección de giro o vista

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190
    # Comprobación dentro de los limites

def inside_window(point):
    """Return True if point inside window boundaries."""
    return -200 < point.x < 190 and -200 < point.y < 190

def move_food():
    """Move food randomly one step at a time."""
    # Generate a random direction (up, down, left, or right)
    direction = randint(0, 3)
    # Define the possible directions (up, down, left, or right)
    directions = [vector(0, 100), vector(0, -100), vector(-100, 0), vector(100, 0)]
    # Move the food in the selected direction if it remains within the window boundaries
    if inside_window(food + directions[direction]):
        food.move(directions[direction])

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
    # Mueve la cabeza en la dirección actual

    # Verificación de límites y colisiones
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        # Muestra un cuadrado rojo
        update()
        return

    snake.append(head)
    # Agrega la nueva posición de la cabeza a la serpiente

    # Si la cabeza alcanza la comida, la serpiente crece y se genera una nueva posición aleatoria para la comida
    if head == food:
        print('Snake:', len(snake))
        #food.x = randrange(-15, 15) * 10
        #food.y = randrange(-15, 15) * 10
        move_food()  # Move food randomly after being eaten
    else:
        snake.pop(0)
        # Elimina la cola de la serpiente

    clear() # Limpia la pantalla

    # Dibuja la serpiente y la comida
    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

# Configuración inicial de la ventana y controles
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()      # Inicia el bucle principal del juego
done()      # Finaliza la ejecución del programa
