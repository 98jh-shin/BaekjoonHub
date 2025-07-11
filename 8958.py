import sys

sys.stdin = open('input.txt', 'r')

# n = int(sys.stdin.readline())
#
# for _ in range(n):
#     ox_list = list(sys.stdin.readline())
#     score = 0
#     total = 0
#     for i in ox_list:
#         if i == "O":
#             score += 1
#             total += score
#         elif i == "X":
#             score = 0
#     print(total)

n = int(input())

for _ in range(n):
    line = sys.stdin.readline().rstrip()
    streak = 0
    total_score = 0
    for mark in line:
        if mark == "O":
            streak += 1
            total_score += streak
        elif mark == "X":
            streak = 0
    print(total_score)


