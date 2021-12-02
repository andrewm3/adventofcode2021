import fileinput

xs = [x.split() for x in fileinput.input()]
h = d = 0
fns = {
    'forward': lambda x, y, z: (x + z, y    ),
    'down':    lambda x, y, z: (x,     y + z),
    'up':      lambda x, y, z: (x,     y - z),
}

for x, y in xs:
    h, d = fns.get(x)(h, d, int(y))

print(h * d)
