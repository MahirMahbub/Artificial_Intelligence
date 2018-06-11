import heapq
import queue
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len( self.elements ) == 0

    def put(self, item, priority):
        heapq.heappush( self.elements, (priority, item) )

    def get(self):
        return heapq.heappop( self.elements )[1]



class Graph(object):
    def __init__(self):
        self.parent = {}
        self.cost = {}
        self._queue = PriorityQueue()

    def A_star_search(self, diagram, start_node, goal_node):
        self._queue.put( start_node, 0 )
        self.parent[start_node] = None
        self.cost[start_node] = 0
        while not self._queue.empty():
            current = self._queue.get()
            if current == goal_node:
                break
            for child in diagram.neighbors(current):
                new_cost = self.cost[current] + diagram.get_cost(child )
                if self.bool_next_child(child, new_cost):
                    self.find_next_node( child, current, goal_node, new_cost )
        #print(self.parent)
        return self.parent, self.cost

    def find_next_node(self, child, current, goal_node, new_cost):
        self.cost[child] = new_cost
        priority = new_cost + self.heuristic( goal_node, child )
        self._queue.put( child, priority )
        self.parent[child] = current

    def bool_next_child(self, child, new_cost):
        return child not in self.cost or new_cost < self.cost[child]

    def heuristic(self, start_node, destination_node):
        (x1, y1) = start_node
        (x2, y2) = destination_node
        return abs( x1 - x2 ) + abs( y1 - y2 )


class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.weights = {}

    def get_cost(self,destination_node):
        return self.weights.get( destination_node, 1 )

    def neighbors(self, co_ordinate):
        x, y = co_ordinate
        results = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        return filter( self.bool_no_wall, filter( self.bool_valid_cocrdinate, results ) )

    def bool_valid_cocrdinate(self, co_ordinate):
        x, y = co_ordinate
        return 0 <= x < self.width and 0 <= y < self.height

    def bool_no_wall(self, co_ordinate):
        return co_ordinate not in self.walls

def draw_tile(graph, co_ordinate, width, kargs):
    point = "."
    if 'cost' in kargs and co_ordinate in kargs['cost']:
        point = "%d" % kargs['cost'][co_ordinate]
    if 'parent' in kargs and kargs['parent'].get( co_ordinate, None ) is not None:
        (x1, y1) = co_ordinate
        (x2, y2) = kargs['parent'][co_ordinate]
        if x2 == x1 + 1: point = ">"
        if x2 == x1 - 1: point = "<"
        if y2 == y1 + 1: point = "v"
        if y2 == y1 - 1: point = "^"
    if 'start' in kargs and co_ordinate == kargs['start']:
        point = "St"
    elif 'goal' in kargs and co_ordinate == kargs['goal']:
        point = "En"
    elif co_ordinate in graph.walls:
        point = "#"
    return point

def draw_grid(graph, width=2, **kargs):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%2s"  % draw_tile(graph, (x, y), width, kargs), end=" ")
        print()


grid = Grid( 10, 10 )
grid.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
grid.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                   (4, 3), (4, 4), (4, 5), (4, 6),
                                   (4, 7), (4, 8), (5, 1), (5, 2),
                                   (5, 3), (5, 4), (5, 5), (5, 6),
                                   (5, 7), (5, 8), (6, 2), (6, 3),
                                   (6, 4), (6, 5), (6, 6), (6, 7),
                                   (7, 3), (7, 4), (7, 5)]}
start, goal = (2, 4), (4,9)
parent, cost = Graph().A_star_search( grid, start, goal )
draw_grid( grid, width=3, parent=parent, start=start, goal=goal )
print()
draw_grid( grid, width=3, cost=cost, start=start, goal=goal )
print()