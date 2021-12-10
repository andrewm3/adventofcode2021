import fileinput

xs = [[c for c in x.rstrip()] for x in fileinput.input()]

brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
errors   = {')': 3, ']': 57, '}': 1197, '>': 25137}
complete = {')': 1, ']': 2,  '}': 3,    '>': 4}

part1 = 0
part2 = []
for x in xs:
    stack = []

    for c in x:
        if c in brackets.keys():
            stack.append(c)
        elif brackets[stack.pop()] != c:
            part1 += errors[c]
            break
    else:
        points = [complete[brackets[c]] for c in reversed(stack)]
        part2.append(reduce(lambda x, y: x * 5 + y, points))

print(part1)
print(sorted(part2)[len(part2)//2])
