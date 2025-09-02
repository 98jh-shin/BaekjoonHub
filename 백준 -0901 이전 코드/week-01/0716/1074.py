import sys

n, x, y = map(int, sys.stdin.readline().split())
count = 0


def z(depth, x, y):
    if depth == 0:
        return
    global count

    half = 2 ** (depth - 1)

    if x < half:
        dx = True
    else:
        dx = False
    if y < half:
        dy = True
    else:
        dy = False

    if dx:
        if dy:
            z(depth - 1, x, y)
        else:
            count += half * half * 1
            z(depth - 1, x, y - half)
    else:
        if dy:
            count += half * half * 2
            z(depth - 1, x - half, y)
        else:
            count += half * half * 3
            z(depth - 1, x - half, y - half)


z(n, x, y)
print(count)

