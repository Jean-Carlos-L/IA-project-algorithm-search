from typing import List
from src.utils.node import Node


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
            return generated_nodes

        children = current_node.get_successors()
        generated_nodes.extend(children)

        stack.extend(reversed(children))

    print("Goal not found.")
    return generated_nodes
