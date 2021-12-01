import fileinput

xs = [int(x) for x in fileinput.input()]
print(sum([1 for i in range(3, len(xs)) if xs[i] + xs[i-1] + xs[i-2] > xs[i-1] + xs[i-2] + xs[i-3]]))
