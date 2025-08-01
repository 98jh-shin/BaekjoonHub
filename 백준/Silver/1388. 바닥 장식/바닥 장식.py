import sys

n, m = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
print(graph)

def dfs(row, col, ch):
    visited[row][col] = True
    if ch == '-' and col == m - 1:
        return
    if ch == '|' and row == n - 1:
        return

    if ch == '-' and graph[row][col + 1] == '-' and not visited[row][col + 1]: # 가로 방향으로
        dfs(row, col + 1, ch)

    elif ch == '|' and graph[row + 1][col] == '|' and not visited[row + 1][col]: # 세로 방향으로
        dfs(row + 1, col, ch)

count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            count += 1
            dfs(i, j, graph[i][j])

print(count)