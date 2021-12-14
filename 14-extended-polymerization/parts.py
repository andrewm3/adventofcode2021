import fileinput
from collections import defaultdict

lines = [x.strip() for x in fileinput.input()]
poly  = lines[0].strip()
rules = dict(x.split(' -> ') for x in lines[2:])

def freqdiff(pairs):
    freq = defaultdict(int)
    for p, f in pairs.items():
        freq[p[0]] += f
        freq[p[1]] += f

    # First and last characters are counted once, not twice.
    freq[poly[0]]  += 1
    freq[poly[-1]] += 1

    return (max(freq.values()) - min(freq.values())) // 2

def solve(steps):
    pairs = {pair: 0 for pair in rules}
    for i in range(len(poly) - 1):
        pairs[poly[i:i+2]] += 1

    for step in range(steps):
        nextpairs = {pair: 0 for pair in rules}
        for p, f in pairs.items():
            nextpairs[p[0] + rules[p]] += f
            nextpairs[rules[p] + p[1]] += f
        pairs = nextpairs

    return pairs

print(freqdiff(solve(10)))
print(freqdiff(solve(40)))
