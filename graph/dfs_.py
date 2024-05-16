import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation
from graph_functions import build_graph, generate_graph
from debug_functions import dfs, component_unite
from update_functions import update


def main(f, *args, **kwargs):
    function = f(*args, **kwargs)

    options = {
        'node_size': 500,  # size of node
        'width': 1,  # line width of edges
        'arrowstyle': '-|>',  # array style for directed graph
        'arrowsize': 18,  # size of arrow
        'edge_color': 'blue',  # edge color
        "with_labels": True,
        "pos": nx.circular_layout(G)
    }

    function_debug = lambda num: update(ax, function, G, mark, options, num)

    fig, ax = plt.subplots(figsize=(6, 4))
    ani = matplotlib.animation.FuncAnimation(fig, function_debug, frames=6, interval=2000,
                                             repeat=True)
    plt.show()


if __name__ == "__main__":
    N = 20
    M = 10

    graph = generate_graph(N, M)

    mark: list[bool] = [False] * N

    G = build_graph(graph)

    main(component_unite, graph, mark)
