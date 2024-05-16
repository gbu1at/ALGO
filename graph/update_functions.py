import networkx as nx


def update(ax, function_debug, G: nx.Graph, mark: list[bool], options: dict, num: int):
    ax.clear()

    color_map = ["green"] * mark.__len__()

    for i in range(mark.__len__()):
        if mark[i]:
            color_map[i] = "red"

    try:
        function_debug.__next__()
    except StopIteration:
        print("functions stop iterable")

    nx.draw(G, node_color=color_map, **options)

    ax.set_xticks([])
    ax.set_yticks([])
