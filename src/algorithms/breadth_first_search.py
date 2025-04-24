from collections import deque
from typing import List, Tuple
from src.utils.node import Node


def reconstruct_path(goal_node: Node) -> List[Node]:
    path = []
    current = goal_node
    while current:
        path.append(current)
        current = current.parent
    return list(reversed(path))


def breadth_first_search(start_node: Node) -> Tuple[List[Node], List[Node]]:
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
            path_to_goal = reconstruct_path(current_node)
            return generated_nodes, path_to_goal

        if current_node.depth % 3 == 0:
            current_node.mutate()

        children = current_node.get_successors()
        generated_nodes.extend(children)
        queue.extend(children)

    print("Goal not found.")
    return generated_nodes, []
