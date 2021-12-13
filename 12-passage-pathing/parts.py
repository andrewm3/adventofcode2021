import fileinput
from collections import defaultdict

conns = [x.rstrip().split('-') for x in fileinput.input()]

g = defaultdict(set)
for a, b in conns:
    g[a].add(b), g[b].add(a)

small = lambda n: n.islower() and n not in ['start', 'end']
big   = lambda n: n.isupper()

def part1(n, p, c):
    return big(n) or n not in p

def part2(n, p, c):
    if big(n) or n not in p:
        return True
    elif n in ['start', 'end']:
        return False

    if any(True for n, x in c.items() if small(n) and x > 1):
        return False

    return small(n)

def dfs(g, a, b, fn, paths, path, c=defaultdict(int)):
    path.append(a)
    c[a] += 1

    for n in g[a]:
        if fn(n, path, c):
            paths = dfs(g, n, b, fn, paths, list(path), c.copy())

    if a == b:
        paths.append(path)

    return paths

print(len(dfs(g, 'start', 'end', part1, [], [])))
print(len(dfs(g, 'start', 'end', part2, [], [])))
