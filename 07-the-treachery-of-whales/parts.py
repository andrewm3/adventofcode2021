import fileinput

xs = sorted(map(int, fileinput.input()[0].strip().split(',')))
m  = xs[len(xs) // 2]

print(sum(abs(x - m) for x in xs))

fuel = lambda y, xs: sum(sum(range(1, abs(x - y) + 1)) for x in xs)

part2 = fuel(xs[0], xs)
for i in range(xs[0] + 1, xs[-1]):
    f = fuel(i, xs)
    if f < part2:
        part2 = f
    else:
        break

print(part2)
