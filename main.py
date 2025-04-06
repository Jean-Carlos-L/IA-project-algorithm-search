from src.algorithms.breadth_first_search import breadth_first_search
from src.utils.problem import MazeProblem

if __name__ == "__main__":
    maze = [
    [' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' '],
    [' ', '#', ' ', '#', '#', ' ', '#', '#', '#', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' '],
    ['#', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
    [' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', ' '],
    [' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' '],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' '],
    [' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ']
]
    initial_mouse = (2, 3)
    initial_cheese = (8, 7)

    problem = MazeProblem(maze, initial_mouse, initial_cheese)

    print("Estado inicial:")
    problem.display_state(problem.initial_state)

    goal_node = breadth_first_search(problem)

    if goal_node:
        print("\nAcciones para llegar al queso:")
        path = goal_node.path()  # Reconstruye el camino desde el nodo inicial
        for i, node in enumerate(path):
            print(f"Paso {i}:")
            problem.display_state(node.state)
            if node.action:
                print(f"Acción tomada: {node.action}\n")
    else:
        print("\nNo se encontró una solución.")
            