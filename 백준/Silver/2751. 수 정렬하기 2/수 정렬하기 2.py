import sys

n = int(input())

nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
result = sorted(nums, key = lambda s: s)
print(*sorted(nums, key = lambda s: s))