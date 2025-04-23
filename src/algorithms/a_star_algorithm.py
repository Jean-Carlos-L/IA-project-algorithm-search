from queue import PriorityQueue
from typing import List
from src.utils.node import Node  # Asegurate de tener la clase Node bien implementada
from src.utils.maze_dynamics import MazeDynamics


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
            return generated_nodes
        
        # Si queremos mutar el laberinto
        if current_node.depth % 3 == 0:  # Cada 3 pasos
            maze_dynamics = MazeDynamics(current_node.maze, current_node.mouse_pos, current_node.cheese_pos)
            new_maze = maze_dynamics.mutate()  # Llamamos al método mutate
        else:
            new_maze = current_node.maze

        children = current_node.get_successors(maze_override=new_maze)
        generated_nodes.extend(children)

        for child in children:
            open_set.put((child.cost + child.heuristic, child))

    print("Goal not found.")
    return generated_nodes
