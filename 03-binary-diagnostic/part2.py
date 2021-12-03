import fileinput

xs = [x.strip() for x in fileinput.input()]
w  = len(xs[0])

def f(l, cmp):
    xs = list(l)
    for i in range(w):
        y = sum(map(lambda x: int(x[i]), xs))

        m = "0"
        if cmp(y, len(xs)):
            m = "1"

        xs = filter(lambda x: x[i] == m, xs)
        if len(xs) == 1:
            return int(xs[0], 2)

cs = f(xs, lambda x, n: x <  n / 2)
og = f(xs, lambda x, n: x >= n / 2)

print(cs * og)
