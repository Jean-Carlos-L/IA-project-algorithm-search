from collections import deque
from typing import List
from src.utils.node import Node


def breadth_first_search(start_node: Node) -> List[Node]:
    queue = deque([start_node])  # Cola para BFS
    generated_nodes = [start_node]  # Todos los nodos generados (para graficar)
    visited_nodes = []  # Opcional: los nodos que se expandieron

    while queue:
        current_node = queue.popleft()
        visited_nodes.append(current_node)

        # Verificamos si es el objetivo
        if current_node.is_goal():
            print("Goal found!")
            return generated_nodes  # Retornamos todos los nodos generados para graficar

        # Expandimos el nodo actual
        children = current_node.get_successors()

        # Guardamos los hijos sin filtrar repeticiones
        generated_nodes.extend(children)

        # En amplitud agregamos al final de la cola
        queue.extend(children)

    print("Goal not found.")
    return generated_nodes

