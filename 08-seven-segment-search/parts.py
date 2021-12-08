import fileinput

xs = [x.split('|')[0].split() for x in fileinput.input()]
ys = [y.split('|')[1].split() for y in fileinput.input()]

digits = {2: 1, 3: 7, 4: 4, 7: 8}
# 5 -> [2, 3, 5], 6 -> [6, 9, 0]

print(sum(sum(1 for n in y if len(n) in digits.keys()) for y in ys))

part2 = 0
for i, x in enumerate(xs):
    numbers = {digits[len(k)]: k for k in x if digits.get(len(k))}
    fives   = [k for k in x if len(k) == 5]
    sixes   = [k for k in x if len(k) == 6]

    numbers[3] = fives.pop(next(i for i, k in enumerate(fives) if set(numbers[1]).issubset(set(k))))
    numbers[6] = sixes.pop(next(i for i, k in enumerate(sixes) if not(set(numbers[1]).issubset(set(k)))))
    numbers[9] = sixes.pop(next(i for i, k in enumerate(sixes) if set(numbers[4]).issubset(set(k))))
    numbers[5] = fives.pop(next(i for i, k in enumerate(fives) if set(k).issubset(set(numbers[9]))))
    numbers[2] = fives.pop()
    numbers[0] = sixes.pop()

    tab = {''.join(sorted(v)): str(k) for k, v in numbers.items()}
    out = int(''.join([tab[''.join(sorted(y))] for y in ys[i]]))

    part2 += out

print(part2)
