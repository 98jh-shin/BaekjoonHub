import sys

n = int(input())

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))

    sum_score = 0

    for j in line[1:]:
        sum_score += j

    average = sum_score / line[0]
    count = 0

    for j in line[1:]:
        if j > average:
            count += 1

    result = count / line[0] * 100


    print(f"{result:.3f}%")
