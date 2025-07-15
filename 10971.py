import sys

sys.stdin = open('input.txt', 'r')

s = int(input())

cost = [list(map(int, sys.stdin.readline().split())) for _ in range(s)]

min_cost = 10000011
current_cost = 0
visited = [False] * s


def dfs(depth, start, current_loc, current_cost):
    global min_cost

    if depth == s - 1:
        if cost[current_loc][start] != 0:
            if min_cost > current_cost + cost[current_loc][start]:
                min_cost = current_cost + cost[current_loc][start]
        return

    for i in range(s):
        if visited[i]:
            continue

        if cost[current_loc][i] == 0:
            continue

        visited[i] = True
        dfs(depth + 1, start, i, current_cost + cost[current_loc][i])
        visited[i] = False

for i in range(s):
    visited[i] = True
    dfs(0, i, i, 0)
    visited[i] = False

print(min_cost)