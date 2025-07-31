import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
a=[list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

start=[]
def startcheck():
    for i in range(n):
        for j in range(n):
            if a[i][j] != 0:
                start.append((a[i][j],i,j,0))


def bfs():
    deque_bfs = deque(start)
    while deque_bfs:
        d, e, f,t = deque_bfs.popleft()
        if t == s:
            return
        for i in range(4):
            ne = e+dx[i]
            nf = f+dy[i]
            if 0<=ne<n and 0<=nf<n:
                if a[ne][nf] ==0:
                    a[ne][nf]=d
                    deque_bfs.append((a[ne][nf], ne, nf, t+1))
startcheck()
start.sort()
bfs()

if len(start) == 0:
    print(0)
else:
    print(a[x-1][y-1])