from typing import Generator
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation
from graph_functions import build_graph, generate_graph, generate_bipartite_graph
from debug_functions import dfs, component_unite, bfs, top_sort, kuhn_algorithm
from update_functions import update


def main(function, frames, interval):
    fig, ax = plt.subplots(figsize=(6, 4))

    options = {
        'node_size': 200,  # size of node
        'width': 2,  # line width of edges
        'arrowstyle': '-|>',  # array style for directed graph
        'arrowsize': 10,  # size of arrow
        "with_labels": True,
        "pos": nx.circular_layout(G)
    }

    function_debug = lambda num: update(ax, function_debug=function, graph=G, mark=mark, options=options,
                                        node_color=node_color, edge_color=edge_color, num=num)

    ani = matplotlib.animation.FuncAnimation(fig, function_debug, frames=frames, interval=interval,
                                             repeat=True)
    plt.show()


if __name__ == "__main__":
    first_comp = 6
    second_comp = 4
    E = 8
    graph = generate_bipartite_graph(first_comp, second_comp, E)

    G = build_graph(graph)
    mark: list[bool] = [False] * (first_comp + second_comp)

    node_color: list[str] = ["red"] * (first_comp + second_comp)
    edge_color: list[str] = ["grey"] * E

    lambda_kuhn_algorithm = kuhn_algorithm(first_comp, second_comp, graph, mark, node_color, edge_color)

    main(lambda_kuhn_algorithm, frames=10000, interval=2000)
