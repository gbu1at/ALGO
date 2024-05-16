def dfs(v: int, graph: list[list[int]], mark: list[bool]):
    mark[v] = True

    yield

    for u in graph[v]:
        if not mark[u]:
            func = dfs(u, graph, mark)
            while True:
                try:
                    yield func.__next__()
                except StopIteration:
                    break


def component_unite(graph: list[list[int]], mark: list[bool]):
    for v in range(graph.__len__()):
        if not mark[v]:
            func = dfs(v, graph, mark)
            while True:
                try:
                    yield func.__next__()
                except StopIteration:
                    break

