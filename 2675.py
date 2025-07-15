import sys

sys.stdin = open('input.txt', 'r')

n = int(input())

# for _ in range(n):
#     temp = ""
#     line = list(sys.stdin.readline().split())
#
#     for i in line[1]:
#         temp += i * int(line[0])
#
#     print(temp)

for _ in range(n):
    c, s = sys.stdin.readline().split()
    c = int(c)
    result = (''.join(c * ch for ch in s))
    print(result)

