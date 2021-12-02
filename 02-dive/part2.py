import fileinput

xs = [x.split() for x in fileinput.input()]
h = d = a = 0
fns = {
    'forward': lambda h, d, a, x: (h + x, d + a * x, a),
    'down':    lambda h, d, a, x: (h,     d,         a + x),
    'up':      lambda h, d, a, x: (h,     d,         a - x),
}

for x, y in xs:
    h, d, a = fns.get(x)(h, d, a, int(y))

print(h * d)
