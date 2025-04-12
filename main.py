from src.algorithms.breadth_first_search import breadth_first_search
from src.algorithms.depth_first_search import depth_first_search
from src.algorithms.a_star_algorithm import a_star_search
from src.views.show_tree import show_tree
from src.utils.problem import MazeProblem

# Función auxiliar para reconstruir el árbol desde el nodo objetivo
def reconstruct_tree(goal_node):
    path = goal_node.path()
    for i in range(len(path) - 1):
        parent = path[i]
        child = path[i + 1]
        if not hasattr(parent, 'children'):
            parent.children = []
        parent.children.append(child)
    return path[0]  # Nodo raíz reconstruido con hijos

if __name__ == "__main__":
    # Definición del laberinto
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
    initial_mouse = (0, 0)
    initial_cheese = (8, 7)

    # Definir el problema
    problem = MazeProblem(maze, initial_mouse, initial_cheese)

    print("Estado inicial:")
    problem.display_state(problem.initial_state)

    # Realizar la búsqueda (descomenta el que prefieras)
    goal_node = breadth_first_search(problem)
    #goal_node = depth_first_search(problem)
    #goal_node = a_star_search(problem)

    if goal_node:
        print("\nAcciones para llegar al queso:")
        path = goal_node.path()  # Reconstruye el camino desde el nodo inicial
        for i, node in enumerate(path):
            print(f"Paso {i}:")
            problem.display_state(node.state)
            if node.action:
                print(f"Acción tomada: {node.action}\n")
                print(f"Costo acumulado: {node.cost}")

                #mostramos los childrens
                print("children " + str([str(child) for child in node.children]))
                
            
        # Mostrar el árbol de búsqueda
        root_node = reconstruct_tree(goal_node)
        show_tree(root_node)


    else:
        print("\nNo se encontró una solución.")
