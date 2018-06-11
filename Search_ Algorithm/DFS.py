
from collections import defaultdict
from typing import List


class Graph(object):

    graph: defaultdict(list)
    searched_element: int

    def __init__(self, searched_element: int):
        self.graph = defaultdict(list)
        assert isinstance(searched_element, int)
        self.searched_element = searched_element

    def add_edge(self, u: int, v: int) -> None:
        assert isinstance(self.graph[u], List)
        self.graph[u].append(v)

    def dfs_recursive(self, v: int, visited: List[int]) -> None:
        assert isinstance(visited, List)
        assert isinstance(v, int)
        visited[v] = True
        print(v)
        if self.searched_element == v:
            print("Found")
            exit()
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_recursive(i, visited)

    def dfs(self) -> None:
        num_child: int = len(self.graph)
        visited: List[bool] = [False] * num_child
        for i in range(num_child):
            if not visited[i]:
                self.dfs_recursive(i, visited)
        print("Not Found")


if __name__ == "__main__":
    g = Graph(1)

    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(1, 2)

    g.dfs()
