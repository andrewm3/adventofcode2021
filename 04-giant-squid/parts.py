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

part1 = part2 = 0
score = lambda n, b: n * sum([x for row in b for (x, y) in row if not y])
bingo = lambda b: any([all([y for (x, y) in row]) for row in b]) or \
                  any([all([y for (x, y) in col]) for col in zip(*b)])
for n in nums:
    boards = [[[(x, y or x == n) for (x, y) in row] for row in b] for b in boards]
    winner = filter(bingo, boards)
    losers = filter(lambda x: not(bingo(x)), boards)

    if len(winner) == 1 and part1 == 0: part1 = score(n, winner[0])
    if len(boards) == 1 and len(losers) == 0:
        part2 = score(n, boards[0])
        break

    boards = losers

print(part1)
print(part2)
