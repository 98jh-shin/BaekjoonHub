import sys

n = int(input())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [False] * n
current_cost = 0
min_cost = 10000012


def dfs(depth, start, current_loc, current_cost):
    global min_cost

    if depth == n - 1:
        if costs[current_loc][start] != 0:
            current_cost += costs[current_loc][start]
            min_cost = min(min_cost, current_cost)
        return

    for i in range(n):
        if visited[i]:
            continue
        if costs[current_loc][i] == 0:
            continue
        if current_cost + costs[current_loc][i] >= min_cost:
            continue

        visited[i] = True
        dfs(depth + 1, start, i, current_cost + costs[current_loc][i])
        visited[i] = False


for i in range(n):
    visited[i] = True
    dfs(0, i, i, 0)
    visited[i] = False

print(min_cost)

