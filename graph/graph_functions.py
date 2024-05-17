import random

import networkx as nx


def build_graph(graph: list[list[int]], directed_graph=False) -> nx.Graph:
    """
    :param graph: граф - список смежностей
    :param directed_graph: параметр, показывающий ориентируемость графа
    :return: граф в классе nx.Graph/nx.DiGraph
    """
    if not directed_graph:
        G = nx.Graph()
    else:
        G = nx.DiGraph()

    for i in range(graph.__len__()):
        G.add_node(i)

    for v in range(graph.__len__()):
        for u in graph[v]:
            G.add_edge(v, u)

    return G


def generate_graph(n: int, m: int, directed_graph=False) -> list[list[int]]:
    """
    :param n: кол-во вершин
    :param m: кол-во ребер, которое нужно провести
    :param directed_graph: параметр, показывающий ориентируемость графа
    :return: произвольный граф/орт.граф
    """
    graph: list[list[int]] = [[] for _ in range(n)]

    assert m <= n * (n - 1) / 2

    for _ in range(m):
        a, b = 0, 0

        while (a == b) or (b in graph[a]):
            a = random.randint(0, n - 1)
            b = random.randint(0, n - 1)

        graph[a].append(b)
        if not directed_graph:
            graph[b].append(a)

    return graph


def generate_bipartite_graph(first_comp: int, second_comp: int, e: int) -> list[list[int]]:
    """
    :param first_comp: кол-во вершин в первой компоненте
    :param second_comp: кол-во вершин во второй компоненте
    :param e: кол-во ребер, которое нужно провести
    :return: произвольный двудольный граф с параметрами выше
    """
    n: int = first_comp + second_comp
    graph: list[list[int]] = [[] for _ in range(n)]

    for _ in range(e):
        a = random.randint(0, first_comp - 1)
        b = random.randint(first_comp, n - 1)

        while (a == b) or (b in graph[a]):
            a = random.randint(0, first_comp - 1)
            b = random.randint(first_comp, n - 1)

        graph[a].append(b)
        graph[b].append(a)

    return graph
