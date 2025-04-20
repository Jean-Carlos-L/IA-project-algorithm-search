import numpy as np
from typing import Optional


class Node:
    DIRECTIONS = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}

    ORDERED_ACTIONS = ["UP", "RIGHT", "DOWN", "LEFT"]

    def __init__(
        self,
        maze: np.ndarray,
        mouse_pos: tuple[int, int],
        cheese_pos: tuple[int, int],
        cost: int = 0,
        heuristic: float = 0.0,
        parent: Optional["Node"] = None,
        action: Optional[str] = None,
    ):
        self.maze = maze
        self.mouse_pos = mouse_pos
        self.cheese_pos = cheese_pos
        self.cost = cost
        self.heuristic = heuristic if heuristic != 0.0 else self.calculate_heuristic()
        self.parent = parent
        self.action = action
        self.depth = 0 if parent is None else parent.depth + 1

    def is_goal(self) -> bool:
        return self.mouse_pos == self.cheese_pos

    def calculate_heuristic(self) -> float:
        x1, y1 = self.mouse_pos
        x2, y2 = self.cheese_pos
        return abs(x1 - x2) + abs(y1 - y2)

    def get_successors(self) -> list["Node"]:
        successors = []
        rows, cols = self.maze.shape

        for action in self.ORDERED_ACTIONS:
            dx, dy = self.DIRECTIONS[action]
            new_x = self.mouse_pos[0] + dx
            new_y = self.mouse_pos[1] + dy

            if 0 <= new_x < rows and 0 <= new_y < cols:
                if self.maze[new_x, new_y] != "#":  # '#' represents wall
                    new_mouse_pos = (new_x, new_y)
                    new_maze = self.maze.copy()  # For now we assume the maze is static
                    new_node = Node(
                        maze=new_maze,
                        mouse_pos=new_mouse_pos,
                        cheese_pos=self.cheese_pos,
                        cost=self.cost + 1,
                        heuristic=0.0,
                        parent=self,
                        action=action,
                    )
                    new_node.heuristic = new_node.calculate_heuristic()
                    successors.append(new_node)

        return successors

    def __eq__(self, other):
        return (
            isinstance(other, Node)
            and self.mouse_pos == other.mouse_pos
            and self.cheese_pos == other.cheese_pos
            and np.array_equal(self.maze, other.maze)
        )

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __hash__(self):
        return hash((self.mouse_pos, self.cheese_pos, self.maze.tobytes()))

    def copy(self):
        return Node(
            self.maze.copy(),
            self.mouse_pos,
            self.cheese_pos,
            self.cost,
            self.heuristic,
            self.parent,
            self.action,
        )

    # def __str__(self):
    #     return f"Mouse: {self.mouse_pos}, Cheese: {self.cheese_pos}, Cost: {self.cost}, Heuristic: {self.heuristic}, Action: {self.action}, Depth: {self.depth}"
    def __str__(self):
        return f"M: {self.mouse_pos}, h: {self.heuristic} g: {self.cost}"
