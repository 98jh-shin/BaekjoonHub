import sys

n, s = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

nums = sorted(nums)

def dfs(depth, current):
    global count

    for i in range(depth, n):
        if current + nums[i] == s:
            count += 1
        dfs(i + 1, current + nums[i])

dfs(0,0)
print(count)
