from collections import defaultdict
import queue as Queue


class Graph( object ):

    def __init__(self, searched_element):
        self.graph = defaultdict( list )
        self.searched_element = searched_element

    def add_edge(self, u, v):
        self.graph[u].append( v )

    def best_first_search(self, node):
        visited = [False] * len( self.graph )
        _queue = Queue.PriorityQueue()
        _queue.put(node)
        try:
            visited[node] = True
        except IndexError as i_e:
            print( "Not Found" )
            return 0
        while not _queue.empty():
            node = _queue.get()
            print( node, end=" " )
            if node == self.searched_element:
                print( "found" )
                return 0
            for i in self.graph[node]:
                if visited[i] == False:
                    _queue.put( i )
                    visited[i] = True
        print( "Not Found" )


if __name__ == "__main__":
    g = Graph( 1 )
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(1, 2)

    g.best_first_search(0)