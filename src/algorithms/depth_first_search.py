from typing import List
from src.utils.node import Node
from src.utils.maze_dynamics import MazeDynamics


def depth_first_search(start_node: Node) -> List[Node]:
    stack = [start_node]  # Pila para DFS
    visited = set()  # Para evitar ciclos
    generated_nodes = [start_node]  # Todos los nodos generados, para graficar

    while stack:
        current_node = stack.pop()

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node.is_goal():
            print("Goal found!")

            # Aquí se arma el camino desde la meta hasta el inicio
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            path.reverse()  # El camino debe ir desde el inicio hasta la meta

            # Agregar el camino al conjunto de nodos generados para la visualización
            generated_nodes.extend(path)

            return (
                generated_nodes,
                path,
            )  # Devuelve los nodos generados y el camino hacia la meta

        if current_node.depth % 3 == 0:
            current_node.mutate()

        children = current_node.get_successors()
        generated_nodes.extend(children)

        # Añadir los hijos a la pila (en orden inverso para DFS)
        stack.extend(reversed(children))

    print("Goal not found.")
    return (
        generated_nodes,
        [],
    )  # Si no se encuentra la meta, retorna el conjunto de nodos generados y una lista vacía
