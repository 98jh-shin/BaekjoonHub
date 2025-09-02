from collections import deque
import sys

M, N, H = map(int, sys.stdin.readline().split())
que = deque()
tomato_parm = []

dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]

for _ in range(H):
    layer = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        layer.append(row)
    tomato_parm.append(layer)


def bfs():
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomato_parm[k][i][j] == 1:
                    que.append((j, i, k))
    while que:
        x, y, z = que.popleft()

        for m in range(6):
            nx = dx[m] + x
            ny = dy[m] + y
            nz = dz[m] + z

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if tomato_parm[nz][ny][nx] == 0:
                    tomato_parm[nz][ny][nx] = tomato_parm[z][y][x] + 1
                    que.append((nx, ny, nz))


bfs()

answer = 0
for k in range(H):
    for j in range(N):
        for i in range(M):
            if tomato_parm[k][j][i] == 0:
                print(-1)
                exit()
            answer = max(answer, tomato_parm[k][j][i])

print(answer - 1)