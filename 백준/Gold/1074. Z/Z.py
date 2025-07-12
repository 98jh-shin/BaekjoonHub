import sys

n, row, col = map(int, sys.stdin.readline().split())

count = 0

def search_z(n, row, col):
    if n == 0:
        return
    global count

    half = 2 ** (n - 1)

    if row < half:
        x = True
    else:
        x = False

    if col < half:
        y = True
    else:
        y = False

    if x:
        if y:
            search_z(n - 1, row, col)
        else:
            count += half * half * 1
            search_z(n - 1, row, col - half)
    else:
        if y:
            count += half * half * 2
            search_z(n - 1, row - half, col)
        else:
            count += half * half * 3
            search_z(n - 1, row - half, col - half)

search_z(n, row, col)
print(count)