import sys

t = int(input())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    docs = list(map(int, sys.stdin.readline().split()))

    q = []
    for i in range(n):
        q.append([i, docs[i]])

    count = 0
    while True:
        if not q:
            break
        find = False
        for i in range(1, len(q)):
            if q[0][1] < q[i][1]:
                q.append(q.pop(0))
                find = True
                break

        if not find:
            cur = q.pop(0)
            count += 1
            if cur[0] == m:
                print(count)
                break
