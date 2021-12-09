import fileinput

hm = [[int(c) for c in x.rstrip()] for x in fileinput.input()]
n  = len(hm) - 1
z  = 9

def adj(x, y, m):
    n = len(m)
    return {(x + dx, y + dy) for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]
            if 0 <= x + dx < n and 0 <= y + dy < n}

def search(x, y, m, v):
    v.add((x, y))
    for i, j in adj(x, y, m) - v:
        if not(m[x][y] < m[i][j] < z):
            continue

        v.add((i, j))
        v = v | search(i, j, m, v)

    return v

lows = {(x, y): h for x, row in enumerate(hm) for y, h in enumerate(row)
        if (x == 0 or hm[x-1][y] > h) and (x == n or hm[x+1][y] > h) and
           (y == 0 or hm[x][y-1] > h) and (y == n or hm[x][y+1] > h)}

basins  = []
visited = set()
for (x, y), low in lows.items():
    if (x, y) in visited:
        continue

    basin = search(x, y, hm, set())
    basins.append(basin)
    visited = visited | basin

print(sum(x + 1 for _, x in lows.items()))
print(reduce(lambda x, y: x * y, sorted(len(b) for b in basins)[-3:]))
