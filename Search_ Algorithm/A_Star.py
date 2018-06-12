import heapq
from builtins import property
from typing import Tuple, List, Dict, Iterator


class PriorityQueue(object):
    elements: List[int]

    def __init__(self) -> None:
        self.elements = []

    @property
    def empty(self) -> bool:
        return len(self.elements) == 0

    def put(self, item: Tuple[int, int], priority: int) -> None:
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> Tuple[int, int]:
        return heapq.heappop(self.elements)[1]


class Grid(object):

    width: int
    height: int
    walls: List[Tuple[int, int]]
    weights: Dict[Tuple[int, int], int]

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.walls = []
        self.weights = {}

    def get_cost(self, destination_node: Tuple[int, int]) -> int:
        return self.weights.get(destination_node, 1)

    def neighbors(self, co_ordinate: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
        (x, y) = co_ordinate
        results: List[Tuple[int, int]] = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        return filter(self.bool_no_wall, filter(self.bool_valid_coordinate, results))

    def bool_valid_coordinate(self, co_ordinate: Tuple[int, int]) -> bool:
        (x, y) = co_ordinate
        return 0 <= x < self.width and 0 <= y < self.height

    def bool_no_wall(self, co_ordinate: Tuple[int, int]) -> bool:
        return co_ordinate not in self.walls


def heuristic(start_node: Tuple[int, int], destination_node: Tuple[int, int]) -> int:
    (x1, y1) = start_node
    (x2, y2) = destination_node
    return abs(x1 - x2) + abs(y1 - y2)


class Graph(object):
    _queue: PriorityQueue
    cost: Dict[Tuple[int, int], int]
    parent: Dict[Tuple[int, int], Tuple[int, int]]

    def __init__(self):
        self.parent = {}
        self.cost = {}
        self._queue = PriorityQueue()

    def a_star_search(self, diagram: Grid, start_node: Tuple[int, int], goal_node: Tuple[int, int]) -> \
            Tuple[dict, dict]:
        self._queue.put(start_node, 0)
        self.parent[start_node] = (-1, -1)
        self.cost[start_node] = 0
        while not self._queue.empty:
            current: Tuple[int, int] = self._queue.get()
            if current == goal_node:
                break
            for child in diagram.neighbors(current):
                new_cost = self.cost[current] + diagram.get_cost(child)
                if self.bool_next_child(child, new_cost):
                    self.find_next_node(child, current, goal_node, new_cost)
        return self.parent, self.cost

    def find_next_node(self, child, current, goal_node, new_cost) -> None:
        self.cost[child] = new_cost
        priority = new_cost + heuristic(goal_node, child)
        self._queue.put(child, priority)
        self.parent[child] = current

    def bool_next_child(self, child, new_cost) -> bool:
        return child not in self.cost or new_cost < self.cost[child]


def draw_tile(graph, co_ordinate, draw_description: dict) -> str:
    point: str = "."
    if 'cost' in draw_description and co_ordinate in draw_description['cost']:
        point = "%d" % draw_description['cost'][co_ordinate]
    if 'parent' in draw_description and  draw_description['parent'].get(co_ordinate, None) is not None and 'path' not in draw_description:
        (x1, y1) = co_ordinate
        (x2, y2) = draw_description['parent'][co_ordinate]
        if x2 == x1 + 1:
            point = "<"
        if x2 == x1 - 1:
            point = ">"
        if y2 == y1 + 1:
            point = "^"
        if y2 == y1 - 1:
            point = "v"
    if 'start' in draw_description and co_ordinate == draw_description['start']:
        point = "St"
    elif 'goal' in draw_description and co_ordinate == draw_description['goal']:
        point = "En"
    elif co_ordinate in graph.walls:
        point = "#"
    elif 'path' in draw_description and co_ordinate in draw_description['path'] :
        (x1, y1) = co_ordinate
        (x2, y2) = draw_description['parent'][co_ordinate]
        if x2 == x1 + 1:
            point = "<"
        if x2 == x1 - 1:
            point = ">"
        if y2 == y1 + 1:
            point = "^"
        if y2 == y1 - 1:
            point = "v"

    return point


def draw_grid(graph, **draw_description) -> None:
    for y in range(graph.height):
        for x in range(graph.width):
            print("%2s" % draw_tile(graph, (x, y), draw_description), end=" ")
        print()


def Shortest_path(came_from: dict, start: Tuple[int, int], goal: Tuple[int, int]) -> List[int]:
    current: Tuple[int, int] = goal
    path: List[int] = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    return path

grid: Grid = Grid(10, 10)
grid.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
grid.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                   (4, 3), (4, 4), (4, 5), (4, 6),
                                   (4, 7), (4, 8), (5, 1), (5, 2),
                                   (5, 3), (5, 4), (5, 5), (5, 6),
                                   (5, 7), (5, 8), (6, 2), (6, 3),
                                   (6, 4), (6, 5), (6, 6), (6, 7),
                                   (7, 3), (7, 4), (7, 5)]}
start: Tuple[int, int] = (2, 4)
goal: Tuple[int, int] = (4, 9)
parent: dict = Graph().a_star_search(grid, start, goal)[0]
cost: dict = Graph().a_star_search(grid, start, goal)[1]
draw_grid(grid, parent=parent, start=start, goal=goal)
print()
draw_grid(grid, cost=cost, start=start, goal=goal)
print()
draw_grid( grid, parent = parent, start=start, goal=goal, path=Shortest_path( parent, start=(2, 4), goal=(4, 9) ) )