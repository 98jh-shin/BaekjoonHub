import sys
from itertools import permutations

sys.stdin = open("../../../input.txt", "r")

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

result = 0

for perm in permutations(nums):
    temp = sum(abs(perm[i] - perm[i + 1]) for i in range(n - 1))
    result = max(result, temp)

print(result)
