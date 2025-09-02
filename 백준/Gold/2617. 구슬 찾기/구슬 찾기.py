import sys

n, m = map(int, sys.stdin.readline().split())

light_list = [[] for _ in range(n + 1)]
heavy_list = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    light_list[i].append(j)
    heavy_list[j].append(i)

def count_light(x):
    visited[x] = True
    global l_count
    for idx in light_list[x]:
        if not visited[idx]:
            count_light(idx)
            l_count += 1

def count_heavy(x):
    visited[x] = True
    global h_count
    for idx in heavy_list[x]:
        if not visited[idx]:
            count_heavy(idx)
            h_count += 1

mid = (n // 2)
count = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    l_count = 0
    h_count = 0
    count_light(i)
    count_heavy(i)
    if l_count > mid:
        count += 1
    elif h_count > mid:
        count += 1
print(count)


