import sys

n = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))
oper = list(map(int, sys.stdin.readline().strip().split()))

min_total = 10 ** 9
max_total = -10 ** 9

def dfs(total, idx):
    global min_total, max_total
    if idx == n:
        min_total = min(min_total, total)
        max_total = max(max_total, total)
        return

    nxt = nums[idx]
    for i in range(4):
        if oper[i] <= 0:
            continue
        oper[i] -= 1

        if i == 0:
            dfs(total + nxt, idx + 1)
        elif i == 1:
            dfs(total - nxt, idx + 1)
        elif i == 2:
            dfs(total * nxt, idx + 1)
        else:
            if total < 0:
                dfs(-(-total // nxt), idx + 1)
            else:
                dfs(total // nxt, idx + 1)

        oper[i] += 1


dfs(nums[0], 1)
print(max_total)
print(min_total)