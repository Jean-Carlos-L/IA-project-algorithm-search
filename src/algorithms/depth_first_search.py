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
            return generated_nodes
        
        if current_node.depth % 3 == 0:  # Cada 3 pasos
            maze_dynamics = MazeDynamics(current_node.maze, current_node.mouse_pos, current_node.cheese_pos)
            new_maze = maze_dynamics.mutate()  # Llamamos al método mutate

        else:
            new_maze = current_node.maze

        children = current_node.get_successors(maze_override=new_maze)
        generated_nodes.extend(children)

        stack.extend(reversed(children))

    print("Goal not found.")
    return generated_nodes
