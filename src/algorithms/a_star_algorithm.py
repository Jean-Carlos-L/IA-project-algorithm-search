import heapq
from src.utils.node import Node

def a_star_search(problem):
    start_state = problem.initial_state
    start_node = Node(
        state=start_state,
        parent=None,
        action=None,
        cost=0,
        heuristic=problem.heuristic(start_state)
    )

    if problem.is_goal(start_state):
        return [start_node.state]

    frontier = []
    heapq.heappush(frontier, start_node)  # Cola de prioridad (min-heap)
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)

        if node.state in explored:
            continue
        explored.add(node.state)

        if node.is_goal(problem):
            return node

        for child in node.expand(problem):
            if child.state not in explored:
                heapq.heappush(frontier, child)

    return None  # No se encontró solución
