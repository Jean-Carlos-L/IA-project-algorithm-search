import time
from copy import deepcopy
from problem import MazeProblem  # Asegúrate que el archivo se llame problem.py

# Mapa inicial (5x5)
maze = [list("     "), list("  #  "), list("     "), list(" ## "), list("     ")]

initial_mouse = (0, 0)
initial_cheese = (4, 4)

problem = MazeProblem(deepcopy(maze), initial_mouse, initial_cheese)

# Movimiento en orden de reloj
actions = ["UP", "RIGHT", "DOWN", "LEFT"]

state = problem.initial_state


def display_maze(maze, mouse, cheese):
    display = deepcopy(maze)
    mx, my = mouse
    cx, cy = cheese
    if (mx, my) == (cx, cy):
        display[mx][my] = "Q"  # Queso encontrado
    else:
        display[mx][my] = "M"
        display[cx][cy] = "C"
    for row in display:
        print("".join(row))
    print()


print("Estado inicial:")
display_maze(problem.maze, *state)

for step in range(10):
    print(f"Paso {step + 1}:")
    for action in actions:
        new_state, cost = problem.result(state, action)
        if new_state:
            state = new_state
            break
    display_maze(problem.maze, *state)
    time.sleep(0.5)
