from queue import PriorityQueue
from typing import List
from src.utils.node import Node  # Asegúrate de tener la clase Node bien implementada


def a_star_search(start_node: Node) -> List[Node]:
    open_set = PriorityQueue()
    open_set.put((start_node.cost + start_node.heuristic, start_node))

    generated_nodes = [start_node]  # Para graficar todo el árbol
    visited = set()

    while not open_set.empty():
        _, current_node = open_set.get()

        # Si ya visitamos este estado con menor costo antes, lo ignoramos
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

        for child in children:
            open_set.put((child.cost + child.heuristic, child))

    print("Goal not found.")
    return (
        generated_nodes,
        [],
    )  # Si no se encuentra la meta, retorna el conjunto de nodos generados y una lista vacía
