import fileinput

lines = [x.strip() for x in fileinput.input()]
dots  = {tuple(map(int, x.split(','))) for x in lines[:lines.index('')]}
folds = [x.split()[-1].split('=') for x in lines[lines.index('')+1:]]

part1 = 0
for fold, n in folds:
    n = int(n)
    if fold == 'y':
        f1 = {(x, y      ) for x, y in dots if y < n}
        f2 = {(x, 2*n - y) for x, y in dots if y > n}
    elif fold == 'x':
        f1 = {(x,       y) for x, y in dots if x < n}
        f2 = {(2*n - x, y) for x, y in dots if x > n}

    dots = f1 | f2

    if part1 == 0:
        part1 = len(dots)

print(part1)

w, h = max(x for x, y in dots) + 1, max(y for x, y in dots) + 1
paper = [[' '] * w for x in range(h)]
for (x, y) in dots:
    paper[y][x] = '#'

for line in paper:
    print(''.join(line))
