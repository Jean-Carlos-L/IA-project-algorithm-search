from collections import deque
from typing import List
from src.utils.node import Node
#from src.utils.maze_dynamics import MazeDynamics  # importar la función dinámica

def breadth_first_search(start_node: Node) -> List[Node]:
    queue = deque([start_node])
    generated_nodes = [start_node]
    visited_nodes = set()

    while queue:
        current_node = queue.popleft()

        if current_node in visited_nodes:
            continue
        visited_nodes.add(current_node)

        if current_node.is_goal():
            print("Goal found!")
            return generated_nodes

        # Si queremos mutar el laberinto
        if current_node.depth % 3 == 0:  # Cada 3 pasos
            # Asegúrate de que mouse_pos y cheese_pos estén presentes en current_node
            current_node.mutate()  # Llamamos al método mutate
            #print(f"\nMaze at depth {current_node.depth} after mutation:")
            #print(new_maze)

        children = current_node.get_successors()
        generated_nodes.extend(children)
        queue.extend(children)

    print("Goal not found.")
    return generated_nodes

