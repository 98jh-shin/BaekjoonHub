import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

water_q = deque()
hedgehog_q = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            water_q.append((i, j))
        elif graph[i][j] == 'S':
            hedgehog_q.append((i, j))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
time = 0

while hedgehog_q:
    time += 1
    for _ in range(len(water_q)):
        x, y = water_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    water_q.append((nx, ny))

    for _ in range(len(hedgehog_q)):
        x, y = hedgehog_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == 'D':
                    print(time)
                    exit()
                elif graph[nx][ny] == '.':
                    graph[nx][ny] = 'S'
                    hedgehog_q.append((nx, ny))
else:
    print("KAKTUS")
