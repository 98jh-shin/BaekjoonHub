import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
max_total = 0
path = []
visited = [False] * n


def dfs(depth):
    global max_total
    if depth == n:
        temp = 0
        for i in range(n - 1):
            temp += abs(path[i] - path[i + 1])
        if max_total < temp:
            max_total = temp
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            path.append(nums[i])
            dfs(depth + 1)
            path.pop()
            visited[i] = False
    return
dfs(0)
print(max_total)