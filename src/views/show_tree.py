import networkx as nx
import matplotlib.pyplot as plt


def plot_tree(nodes):
    G = nx.DiGraph()

    for node in nodes:
        node_id = id(node)
        label = str(node)  # o lo que prefieras mostrar como texto

        G.add_node(node_id, label=label)

        if node.parent:
            parent_id = id(node.parent)
            G.add_edge(parent_id, node_id)

    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")

    # Dibujar nodos con etiquetas
    labels = nx.get_node_attributes(G, "label")
    nx.draw(
        G,
        pos,
        labels=labels,
        with_labels=True,
        node_size=1500,
        node_color="skyblue",
        font_size=10,
        font_weight="bold",
        arrows=True,
    )

    plt.show()
