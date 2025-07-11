import sys

# sys.stdin = open('input.txt', 'r')

# max_value = 0
# for i in range(9):
#     temp = int(sys.stdin.readline())
#     if max_value < temp:
#         max_value = temp
#         index = i + 1
#
#
# print(max_value)
# print(index)

nums = [list(map(int, sys.stdin.readine()) for _ in range(9))]

max_value = max(nums)
index = nums.index(max_value) + 1

print(max_value)
print(index)