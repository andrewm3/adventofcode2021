import fileinput

lines  = [x.rstrip() for x in fileinput.input()]
nums   = map(int, lines[0].split(','))
boards = []

w = h = 5
i = 0
for line in lines[1:]:
    if line == "":
        boards.append([[] * w for x in range(h)])
        i = 0
    else:
        boards[-1][i] = [(int(x), False) for x in line.split()]
        i += 1

score = 0
for n in nums:
    boards = [[[(x, y or x == n) for (x, y) in row] for row in b] for b in boards]
    winner = filter(lambda b: any([all([y for (x, y) in row]) for row in b]) or
                              any([all([y for (x, y) in col]) for col in zip(*b)]),
                    boards)
    if len(winner) == 1:
        score = n * sum([x for row in winner[0] for (x, y) in row if not y])
        break

print(score)
