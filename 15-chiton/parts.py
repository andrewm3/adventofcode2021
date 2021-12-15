import fileinput
import heapq

risks = [[int(c) for c in x.strip()] for x in fileinput.input()]
start = (0, 0)

class PriorityQueue:
    def __init__(self):
        self.nodes = []

    def empty(self):
        return not self.nodes

    def put(self, node, priority):
        heapq.heappush(self.nodes, (priority, node))

    def get(self):
        return heapq.heappop(self.nodes)[1]

class Grid:
    def __init__(self, width, height, costs):
        self.width  = width
        self.height = height
        self.costs  = costs

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def adj(self, (x, y)):
        neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        return {(x + dx, y + dy) for dx, dy in neighbours if self.in_bounds(x + dx, y + dy)}

    def cost(self, (x1, y1), (x2, y2)):
        return self.costs[y2][x2]

def heuristic((x1, y1), (x2, y2)):
    return abs(x2 - x1) + abs(y2 - y1)

# f(n) = g(n) + h(n)
def astar(grid, start, end, h=heuristic):
    open = PriorityQueue()
    open.put(start, 0)

    path = {}
    cost = {}
    path[start] = None
    cost[start] = 0

    while not open.empty():
        current = open.get()

        if current == end:
            break

        for adj in grid.adj(current):
            g = cost[current] + grid.cost(current, adj)
            if adj not in cost or g < cost[adj]:
                f = g + h(adj, end)

                open.put(adj, f)
                cost[adj]  = g
                path[next] = current

    return path, cost

def solve(costs):
    width  = len(costs[0])
    height = len(costs)
    end    = (width - 1, height - 1)

    grid = Grid(width, height, costs)
    path, cost = astar(grid, start, end)
    return cost[end]

def part1():
    return solve(risks)

def part2():
    tiles = []
    for i in range(5):
        for y, costs in enumerate(risks):
            line = []
            for j in range(5):
                for x, cost in enumerate(costs):
                    r = cost + i + j
                    line.append((r, r - 9)[r > 9])
            tiles.append(line)

    return solve(tiles)

print(part1())
print(part2())
