import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
max_num = 0
path = []
visited = [False] * n

num_list = list(map(int, sys.stdin.readline().split()))


def dfs(depth):
    global max_num

    if depth == n:
        temp = 0

        for i in range(n - 1):
            temp += abs((path[i] - path[i + 1]))
            if max_num < temp:
                max_num = temp
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            path.append(num_list[i])
            dfs(depth + 1)

            path.pop()
            visited[i] = False


dfs(0)
print(max_num)