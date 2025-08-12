import sys

T = int(sys.stdin.readline())
def greedy(n):
    arr = [0 for i in range(n)]
    for _ in range(n):
        i, x = map(int, sys.stdin.readline().split())
        arr[i-1] = x
    count = 0
    min_g2 = n + 1
    for t2 in arr:
        if t2 < min_g2:
            count += 1
            min_g2 = t2

    return count

for _ in range(T):
    N = int(sys.stdin.readline())
    print(greedy(N))