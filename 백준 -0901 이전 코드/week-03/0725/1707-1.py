import sys

n = int(sys.stdin.readline().rstrip())


def dfs(cur, col):
    color[cur] = col
    for nxt in con[cur]:
        if color[nxt] == 0:
            if not dfs(nxt, -col):
                return False
        else:
            if color[nxt] == color[cur]:
                return False
    return True

for _ in range(n):
    i, j = map(int, sys.stdin.readline().split())
    color = [0] * (i + 1)
    con = [[] for _ in range(i + 1)]
    for _ in range(j):
        a, b = map(int, sys.stdin.readline().split())
        con[a].append(b)
        con[b].append(a)

    is_bipartite = True
    for x in range(1, i + 1):
        if color[x] == 0:
            is_bipartite = dfs(x, 1)
            if not is_bipartite:
                break

    print("YES" if is_bipartite else "NO")
