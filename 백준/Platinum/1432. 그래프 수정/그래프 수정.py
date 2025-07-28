import sys
import heapq
n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for i in range(1, n + 1):
    input_row = list(map(int, sys.stdin.readline().rstrip()))

    for j in range(len(input_row)):
        if input_row[j] == 1:
            graph[j + 1].append(i)
            in_degree[i] += 1

q = []
for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(q, -i)

result = []
out_list = []
while q:
    cur = -heapq.heappop(q)
    result.append(cur)
    for nxt in graph[cur]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            heapq.heappush(q, -nxt)

if len(result) != n:
    print(-1)
    exit()

res = [0] * (n + 1)
count = n
for node in result:
    res[node] = count
    count -= 1

print(*res[1:])