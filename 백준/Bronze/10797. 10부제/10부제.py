import sys

day_list = [False] * 10
day_list[int(input())] = True
count = 0

for i in list(map(int, sys.stdin.readline().split())):
    if day_list[i]:
        count += 1

print(count)