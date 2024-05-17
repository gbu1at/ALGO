from typing import Generator

import networkx as nx


def update(ax, function_debug: Generator, graph: nx.Graph, mark: list[bool], options: dict, node_color, edge_color, num: int):
    """
    :param ax:
    :param function_debug: передается генератор функции, которую необходимо отдебажить
    :param graph: граф в классе nx.Graph
    :param mark:
    :param options:
    :param node_color: цвет вершин на данном шаге ( динамически изменяется в вызовах function_debug )
    :param num: номер итерации функции update
    :return:
    """
    ax.clear()

    ax.set_title(f"{num}")

    nx.draw(graph, node_color=node_color, edge_color=edge_color, **options)

    ax.set_xticks([])
    ax.set_yticks([])

    try:
        function_debug.__next__()
    except StopIteration:
        print("functions stop iterable")
