import fileinput

xs    = map(int, [x.rstrip().split(',') for x in fileinput.input()][0])
days1 = 80
days2 = 256

ys = [0] * 9
for x in xs: ys[x] += 1

for d in range(days2):
    y0, ys = ys[0], ys[1:]
    ys[6] += y0
    ys.append(y0)

    if d + 1 == days1: print(sum(ys))

print(sum(ys))
