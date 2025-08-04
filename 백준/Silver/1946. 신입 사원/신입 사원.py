import sys

T = int(sys.stdin.readline())
def greedy(n):
    arr = []
    for i in range(n):
        t1, t2 = map(int, sys.stdin.readline().split())
        arr.append((t1, t2))
    arr.sort()

    count = 0
    min_g2 = n + 1
    for _, t2 in arr:
        if t2 < min_g2:
            count += 1
            min_g2 = t2

    return count

for _ in range(T):
    N = int(sys.stdin.readline())
    print(greedy(N))