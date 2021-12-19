import fileinput
import json
from itertools import permutations
from math import ceil

def main():
    inputs  = (x.rstrip() for x in fileinput.input())
    numbers = map(parse, inputs)
    result  = reduce(add, numbers)

    print(magnitude(result))
    print(max(magnitude(add(a, b)) for a, b in permutations(numbers, 2)))

def parse(s):
    num   = []
    depth = -1
    for c in s:
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        elif c.isdigit():
            num.append((int(c), depth))

    return num

def add(a, b):
    num = []
    num.extend([(n, d + 1) for n, d in a])
    num.extend([(n, d + 1) for n, d in b])

    return solve(num)

def solve(num):
    while True:
        num, exploded = explode(num)
        if exploded:
            continue

        num, splitted = split(num)
        if splitted:
            continue

        break

    return num

def explode(num, depth=4):
    for i, (n, d) in enumerate(num):
        if d != depth:
            continue

        # To the left:
        if i > 0:
            num[i - 1] = (num[i - 1][0] + n, num[i - 1][1])

        # And to the right:
        if i + 2 < len(num):
            num[i + 2] = (num[i + 2][0] + num[i + 1][0], num[i + 2][1])

        # Replace with 0:
        num[i:i + 2] = [(0, d - 1)]

        return num, True

    return num, False

def split(num):
    for i, (n, d) in enumerate(num):
        if n > 9:
            num[i:i + 1] = [(n // 2, d + 1), (int(ceil(n / 2.0)), d + 1)]
            return num, True

    return num, False

def magnitude(num, depth=4):
    for i in reversed(range(0, depth)):
        reduced = True
        while reduced:
            num, reduced = magnitude_reduce(num, i)

    return num[0][0]

def magnitude_reduce(num, depth):
    for i, (n, d) in enumerate(num):
        if d != depth:
            continue

        num[i:i + 2] = [(3 * n + 2 * num[i + 1][0], d - 1)]

        return num, True

    return num, False

if __name__ == '__main__':
    main()

assert magnitude(parse('[[1,2],[[3,4],5]]')) == 143
assert magnitude(parse('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')) == 1384
assert magnitude(parse('[[[[1,1],[2,2]],[3,3]],[4,4]]')) == 445
assert magnitude(parse('[[[[3,0],[5,3]],[4,4]],[5,5]]')) == 791
assert magnitude(parse('[[[[5,0],[7,4]],[5,5]],[6,6]]')) == 1137
assert magnitude(parse('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')) == 3488
