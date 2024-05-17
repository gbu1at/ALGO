from collections import deque

default_type_graph = list[list[int]]


def dfs(v: int, graph: default_type_graph, mark: list[bool], node_color: list[str], edge_color: list[str]):
    """
    :param v:
    :param graph:
    :param mark:
    :param node_color:
    :return:
    """
    mark[v] = True
    node_color[v] = "green"

    yield

    for u in graph[v]:
        if not mark[u]:
            func = dfs(u, graph, mark, node_color, edge_color)
            while True:
                try:
                    yield func.__next__()
                except StopIteration:
                    break


def component_unite(graph: default_type_graph, mark: list[bool], node_color: list[str], edge_color: list[str]):
    """
    :param graph:
    :param mark:
    :param node_color:
    :return:
    """
    for v in range(graph.__len__()):
        if not mark[v]:
            func = dfs(v, graph, mark, node_color, edge_color)
            while True:
                try:
                    yield func.__next__()
                except StopIteration:
                    break


def bfs(v: int, graph: default_type_graph, mark: list[bool], node_color: list[str], edge_color: list[str]):
    """
    :param v:
    :param graph:
    :param mark:
    :param node_color:
    :return:
    """
    q: deque[int] = deque()
    q.append(v)

    while q.__len__() != 0:
        v = q.popleft()

        mark[v] = True
        node_color[v] = "green"

        yield

        for u in graph[v]:
            if not mark[u]:
                q.append(u)


def top_sort(graph: default_type_graph, mark: list[int], node_color: list[str], edge_color: list[str]) -> list:
    def _dfs_top_sort(v: int, graph: default_type_graph, mark: list[int], node_color: list[str], result: list[int]):
        """
        :param v:
        :param graph:
        :param mark:
        :param node_color:
        :param result:
        :return:
        """
        mark[v] = 1
        node_color[v] = "gray"
        result.append(v)

        yield

        for u in graph[v]:
            if mark[u] == 0:
                func = _dfs_top_sort(u, graph, mark, node_color, result)
                while True:
                    try:
                        yield func.__next__()
                    except StopIteration:
                        break
            elif mark[v] == 1:
                print("FIND CIRCLE!!!")

        mark[v] = 2

        yield

        node_color[v] = "green"

    result = []
    for v in range(graph.__len__()):
        if not mark[v]:
            local_result = []
            func = _dfs_top_sort(v, graph, mark, node_color, local_result)
            while True:
                try:
                    yield func.__next__()
                except StopIteration:
                    break
            result.extend(list(reversed(local_result)))

    return result


def kuhn_algorithm(first_comp: int, second_comp: int, graph: default_type_graph, mark: list[bool],
                   node_color: list[str], edge_color: list[str]):
    def _dfs_kuhn_algorithm(v: int, graph: default_type_graph, mt: list[int], answer: list):
        if mark[v]:
            answer[0] = False
            return

        mark[v] = True
        node_color[v] = "green"

        yield

        for u in graph[v]:

            if mt[u] == -1:
                mt[u] = v
                edge_color[indexes[f"{v}${u}"]] = "blue"
                answer[0] = True
                node_color[v] = "red"
                yield
                return
            local_answer = [False]
            func = _dfs_kuhn_algorithm(mt[u], graph, mt, local_answer)
            while True:
                try:
                    yield func.__next__()
                except StopIteration:
                    if local_answer[0]:
                        edge_color[indexes[f"{mt[u]}${u}"]] = "grey"
                        mt[u] = v
                        edge_color[indexes[f"{v}${u}"]] = "blue"
                        node_color[v] = "red"
                        answer[0] = True
                        yield
                        return
                    break

        answer[0] = False
        node_color[v] = "red"

    indexes: dict[str:int] = {}
    it = 0

    for v in range(graph.__len__()):
        for u in graph[v]:
            indexes[f"{v}${u}"] = it
            it += 1

    cnt = 0

    mt = [-1] * (first_comp + second_comp)
    for v in range(first_comp):
        for _ in range(mark.__len__()):
            mark[_] = False
            node_color[_] = "red"

        yield

        answer = [False]
        func = _dfs_kuhn_algorithm(v, graph, mt, answer)

        while True:
            try:
                yield func.__next__()
            except StopIteration:
                if answer[0]:
                    cnt += 1
                break
        #
        # for u in range(first_comp, first_comp + second_comp):
        #     if mt[u] != -1:
        #         edge_color[indexes[f"{mt[u]}${u}"]] = "red"

    print(cnt)
