import fileinput

grid  = [[int(c) for c in x.rstrip()] for x in fileinput.input()]
w, h  = len(grid[0]), len(grid)
limit = 9

adj = lambda x, y: {
        (x + dx, y + dy) for dx, dy in [(-1, 0),   (0, 1), (1, 0), (0, -1),
                                        (-1, -1), (-1, 1), (1, 1), (1, -1)]
        if 0 <= x + dx < w and 0 <= y + dy < h
        }

steps = []
while True:
    grid = [[e + 1 for e in row] for row in grid]

    flashes = [(x, y) for y, row in enumerate(grid) for x, e in enumerate(row) if e > limit]
    for x, y in flashes:
        for dx, dy in adj(x, y):
            grid[dy][dx] += 1
            if grid[dy][dx] == limit + 1:
                flashes.append((dx, dy))

    grid = [[(e, 0)[e > limit] for e in row] for row in grid]

    steps.append(len(flashes))
    if steps[-1] == w * h:
        break

print(sum(x for x in steps[:100]))
print(len(steps))
