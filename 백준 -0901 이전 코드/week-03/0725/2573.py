import sys

sys.stdin = open('../../../input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ice_loc = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            ice_loc.append((i, j))

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] > 0:
            dfs(nx, ny)

def next_year(ice_loc):
    melt = [[0] * m for _ in range(n)]
    for x, y in ice_loc:
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] <= 0:
                sea += 1
        melt[x][y] = sea

    new_ice_loc = []
    for x, y in ice_loc:
        if graph[x][y] - melt[x][y] > 0:
            graph[x][y] -= melt[x][y]
            new_ice_loc.append((x, y))
        else:
            graph[x][y] = 0

    return new_ice_loc

year_count = 0
while ice_loc:
    year_count += 1
    ice_loc = next_year(ice_loc)

    visited = [[False] * m for _ in range(n)]
    count = 0
    for x, y in ice_loc:
        if not visited[x][y]:
            dfs(x, y)
            count += 1

    if count >= 2:
        print(year_count)
        break
else:
    print(0)


