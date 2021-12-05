import fileinput

inputs = [x.split() for x in fileinput.input()]
lines  = [(map(int, x[0].split(',')), map(int, x[2].split(','))) for x in inputs]

w = h = 1000
part1 = [[0] * w for x in range(h)]
part2 = [[0] * w for x in range(h)]

for ((x1, y1), (x2, y2)) in lines:
    x, y = x1, y1
    v, h = x1 == x2, y1 == y2
    while (x <= x2, x >= x2)[x1 > x2] and (y <= y2, y >= y2)[y1 > y2]:
        part2[x][y] += 1
        if h or v: part1[x][y] += 1
        if not v: x += (1, -1)[x1 > x2]
        if not h: y += (1, -1)[y1 > y2]

print(sum(1 for row in part1 for x in row if x > 1))
print(sum(1 for row in part2 for x in row if x > 1))
