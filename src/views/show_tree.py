import networkx as nx
import matplotlib.pyplot as plt


def plot_tree(nodes, path=None):
    G = nx.DiGraph()
    path_ids = set()

    if path:
        path_ids = {id(node) for node in path}

    for node in nodes:
        node_id = id(node)
        label = str(node)
        G.add_node(node_id, label=label)

        if node.parent:
            parent_id = id(node.parent)
            G.add_edge(parent_id, node_id)

    fig_width = max(10, len(nodes) * 0.6)
    fig_height = max(5, len(nodes) * 0.15)
    plt.figure(figsize=(fig_width, fig_height))

    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    labels = nx.get_node_attributes(G, "label")

    node_colors = [
        "lightgreen" if node_id in path_ids else "skyblue" for node_id in G.nodes()
    ]

    path_edges = set()
    if path and len(path) > 1:
        path_edges = {(id(path[i]), id(path[i + 1])) for i in range(len(path) - 1)}

    edge_colors = ["green" if edge in path_edges else "gray" for edge in G.edges()]

    nx.draw(
        G,
        pos,
        labels=labels,
        with_labels=True,
        node_size=800,
        node_color=node_colors,
        edge_color=edge_colors,
        font_size=8,
        font_weight="bold",
        arrows=True,
    )

    plt.tight_layout()
    plt.show()
