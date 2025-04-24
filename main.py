import numpy as np
from src.utils.node import Node
from src.algorithms.depth_first_search import depth_first_search
from src.algorithms.breadth_first_search import breadth_first_search
from src.algorithms.a_star_algorithm import a_star_search
from src.views.show_tree import plot_tree
from src.views.config_initial_state import choose_file_and_load

if __name__ == "__main__":
    mouse_pos, cheese_pos, maze, algorithm = choose_file_and_load()
    start_node = Node(maze, mouse_pos, cheese_pos)
    start_node.heuristic = start_node.calculate_heuristic()

    if algorithm == "DFS":
        print("Using Depth First Search")
        all_nodes, path = depth_first_search(start_node)

    if algorithm == "BFS":
        print("Using Breadth First Search")
        all_nodes, path = breadth_first_search(start_node)

    if algorithm == "A*":
        print("Using A* Search")
        all_nodes, path = a_star_search(start_node)

    plot_tree(all_nodes, path)
