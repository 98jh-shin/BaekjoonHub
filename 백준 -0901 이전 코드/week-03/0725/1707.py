import sys

n = int(sys.stdin.readline().rstrip())

def dfs(cur, col):
    color[cur] = col
    for nxt in con[cur]:
        if color[nxt] == 0:
            if not dfs(nxt, -col):
                return False
        elif color[nxt] == color[cur]:
            return False
    return True

for _ in range(n):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    color = [0] * (i + 1)
    con = [[] for _ in range(i + 1)]
    for _ in range(j):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        con[x].append(y)
        con[y].append(x)

    is_bipartite = True
    for k in range(1, i + 1):
        if color[k] == 0:
            is_bipartite = dfs(k, 1)
            if not is_bipartite:
                break
    print("YES" if is_bipartite else "NO")
