class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = (
            state  # Representa el estado actual (posición del ratón, queso, paredes)
        )
        self.parent = parent  # Nodo padre
        self.action = action  # Acción que llevó a este nodo (movimiento del ratón)
        self.cost = cost  # Costo desde el nodo raíz (g(n))
        self.heuristic = heuristic  # Heurística estimada al objetivo (h(n))

    def expand(self, problem):
        """
        Devuelve una lista de nodos hijos aplicando todas las acciones posibles
        según el orden de prioridad: arriba, derecha, abajo, izquierda.
        """
        children = []
        for action in ["UP", "RIGHT", "DOWN", "LEFT"]:
            next_state, step_cost = problem.result(self.state, action)
            if next_state is not None:
                child = Node(
                    state=next_state,
                    parent=self,
                    action=action,
                    cost=self.cost + step_cost,
                    heuristic=problem.heuristic(next_state),
                )
                children.append(child)
        return children

    def is_goal(self, problem):
        """Verifica si el nodo actual es un estado objetivo (el ratón encuentra el queso)."""
        return problem.is_goal(self.state)

    def path(self):
        """Reconstruye el camino desde la raíz hasta este nodo."""
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        return list(reversed(p))

    def __lt__(self, other):
        """Permite comparar nodos por f(n) = g(n) + h(n) (útil para A*)."""
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
