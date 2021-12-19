import fileinput
import re

def main():
    x1, x2, y1, y2 = map(int, re.findall('-?\d+', next(fileinput.input())))
    target = ((x1, x2), (y1, y2))

    ymax = hits = 0
    for vx in range(1, x2 + 1):
        for vy in range(y1, 1000):
            peak = fire(vx, vy, target)
            if peak is not None:
                ymax = max(peak, ymax)
                hits = hits + 1

    print(ymax)
    print(hits)

def fire(vx, vy, target):
    ymax = 0
    x, y = 0, 0

    while not miss(x, y, vx, vy, target):
        x, y, vx, vy = step(x, y, vx, vy)
        ymax = max(y, ymax)

        if hit(x, y, target):
            return ymax

    return None

def step(x, y, vx, vy):
    return x + vx, y + vy, vx + (0, 1)[vx < 0] + (0, -1)[vx > 0], vy - 1

def hit(x, y, target):
    ((x1, x2), (y1, y2)) = target
    return x1 <= x <= x2 and y1 <= y <= y2

def miss(x, y, vx, vy, target):
    ((x1, x2), (y1, y2)) = target
    return x > x2 or (vx == 0 and x < x1) or (y < y1 and vy < 0)

if __name__ == '__main__':
    main()
