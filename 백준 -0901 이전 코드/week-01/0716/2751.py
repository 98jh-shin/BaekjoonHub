import sys

sys.stdin = open('../../../input.txt', 'r')

n = int(input())

nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

print(*sorted(nums, key = lambda s: s))
# result = sorted(nums, key = lambda s: s)
# print(*result)
