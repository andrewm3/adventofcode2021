import fileinput

x = float('inf')
count = 0
for line in fileinput.input():
    n = int(line)
    if n > x:
        count += 1
    x = n

print(count)
