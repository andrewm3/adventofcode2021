import fileinput

xs = [x.strip() for x in fileinput.input()]
xn = len(xs)
w  = len(xs[0])
ys = [0] * w

for x in xs:
    for i, c in enumerate(x):
        ys[i] += int(c)

e = g = ""
for y in ys:
    if y > xn / 2:
        e, g = e + "0", g + "1"
    else:
        e, g = e + "1", g + "0"

print(int(e, 2) * int(g, 2))
