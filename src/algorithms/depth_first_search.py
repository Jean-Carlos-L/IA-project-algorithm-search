from src.utils.node import Node

def depth_first_search(problem):
    start_state = problem.initial_state
    start_node = Node(state=start_state, parent=None, action=None, cost=0)

    if problem.is_goal(start_state):
        return [start_node.state]

    stack = [start_node]
    explored = set()

    while stack:
        node = stack.pop()

        if node.state in explored:
            continue
        explored.add(node.state)

        for action in ['UP', 'RIGHT', 'DOWN', 'LEFT']:
            result = problem.result(node.state, action)
            if result is None:
                continue
            next_state, cost = result
            if next_state is None:
                continue

            child_node = Node(state=next_state, parent=node, action=action, cost=node.cost + cost)

            node.children = child_node.expand(problem)

            if problem.is_goal(next_state):
                return child_node

            stack.append(child_node)

    return None  # Si no se encuentra solución
