import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


for i in range(1, n + 1):
    graph[i] = merge_sort(graph[i])




def dfs(x):
    visited[x] = True
    print(x, end=" ")
    for i in graph[x]:

        if not visited[i]:
            dfs(i)


def bfs(x):
    queue = deque([x])
    visited[x] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (n + 1)
dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)


