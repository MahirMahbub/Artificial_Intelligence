
from collections import defaultdict
from math import ceil
from typing import List

import math


class Graph(object):

    graph: defaultdict(list)
    searched_element: int

    def __init__(self, searched_element: int):
        self.graph = defaultdict(list)
        assert isinstance(searched_element, int)
        self.searched_element = searched_element
        self.value = 0

    def add_edge(self, u: int, v: int) -> None:
        assert isinstance(self.graph[u], List)
        self.graph[u].append(v)

    def dfs_recursive(self, v: int, visited: List[int], turn: bool, height: int, depth: int) -> None:
        assert isinstance(visited, List)
        assert isinstance(v, int)
        visited[v] = True
        depth+=1
        print(depth, height)
        for i in self.graph[v]:
            if not visited[i]:
                print("sdd"+str(i))
                if turn:
                    self.value = self.dfs_recursive(i, visited, False, height, depth)
                    print(self.value)
                else:
                    self.value = self.dfs_recursive(i, visited, True, height, depth)
                    print( self.value )
        if height%2==1:
            if depth == height:
                print(max([-1]+self.graph[v]))
                return max([self.value]+self.graph[v])
            else:
                print( max([self.value]+self.graph[v] ) )
                return  max([self.value]+self.graph[v])
        else:
            if depth == height:
                print([233252525]+self.graph[v] )
                return min([self.value]+self.graph[v])
            else:
                print([self.value]+self.graph[v] )
                return  min([self.value]+self.graph[v])


    def dfs(self, height: int) -> None:
        num_child: int = len(self.graph)
        depth: int = 0
        value:int
        visited: List[bool] = [False] * num_child
        for i in range(num_child):
            if not visited[i]:
                value = self.dfs_recursive(i, visited,True, height, depth)
        print(value)
        print("Not Found")


if __name__ == "__main__":
    g = Graph(1)

    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    height = int(math.ceil(math.log2( 6 )))
    g.dfs(height)
