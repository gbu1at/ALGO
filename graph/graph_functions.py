import random

import networkx as nx


def build_graph(graph: list[list[int]]) -> nx.Graph:
    G = nx.Graph()

    for i in range(graph.__len__()):
        G.add_node(i)

    for v in range(graph.__len__()):
        for u in graph[v]:
            G.add_edge(v, u)

    return G


def generate_graph(n: int, m: int) -> list[list[int]]:
    graph: list[list[int]] = [[] for _ in range(n)]

    assert m <= n * (n - 1) / 2

    for _ in range(m):
        a, b = 0, 0
        while a == b:
            a = random.randint(0, n - 1)
            b = random.randint(0, n - 1)

        graph[a].append(b)
        graph[b].append(a)

    return graph
