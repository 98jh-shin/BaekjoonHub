import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

visited = [False] * (k + 1)
visited[0] = True

count = [0] * (k + 1)

q = deque()
q.append(0)

while q:
    cur = q.popleft()
    for coin in coins:
        res = cur + coin
        if res > k:
            continue
        if res == k:
            count[res] = count[cur] + 1
            print(count[k])
            exit()
        if not visited[res]:
            visited[res] = True
            count[res] = count[cur] + 1
            q.append(res)
else:
    print(-1)