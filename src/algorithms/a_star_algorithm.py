from queue import PriorityQueue
from typing import List
from src.utils.node import Node


def a_star_search(start_node: Node) -> List[Node]:
    open_set = PriorityQueue()
    open_set.put((start_node.cost + start_node.heuristic, start_node))

    generated_nodes = [start_node]
    visited = set()

    while not open_set.empty():
        _, current_node = open_set.get()

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node.is_goal():
            print("Goal found!")

            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            path.reverse()

            generated_nodes.extend(path)

            return (
                generated_nodes,
                path,
            )

        if current_node.depth % 3 == 0:
            current_node.mutate()
            current_node.cheese_pos = current_node.move_cheese(current_node.cheese_pos)

        children = current_node.get_successors()
        generated_nodes.extend(children)

        for child in children:
            open_set.put((child.cost + child.heuristic, child))

    print("Goal not found.")
    return (
        generated_nodes,
        [],
    )
