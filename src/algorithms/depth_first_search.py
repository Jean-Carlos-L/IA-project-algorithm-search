from typing import List
from src.utils.node import Node


def depth_first_search(start_node: Node) -> List[Node]:
    stack = [start_node]
    visited = set()
    generated_nodes = [start_node]

    while stack:
        current_node = stack.pop()

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

        stack.extend(reversed(children))

    print("Goal not found.")
    return (
        generated_nodes,
        [],
    )
