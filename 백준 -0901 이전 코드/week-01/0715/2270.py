import sys

n = int(input())
a ,b , c = map(int, sys.stdin.readline().split())

disks = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

def hanoi(n, start, end, temp):
    if n == 1:
        print(start, end)
        return
    elif n > 1:
        hanoi(n - 1, start, temp, end)
        print(start, end)
        hanoi(n - 1, temp, end, start)

max_disk_idx = 0
idx = 0
for i in range(n - 1):
    if disks[i][0] < disks[i + 1][0]:
        max_disk_idx = i + 1

for i in range(n):
    if i == max_disk_idx:
        continue
    else:
        if disks[idx][0] < disks[i][0]:
            idx = i




"""
s = int(input())

def hanoi(n, start, end, temp):
    if n > 20:
        return
    elif n == 1:
        print(start, end)
        return
    elif n > 1:
        hanoi(n - 1, start, temp, end)
        print(start, end)
        hanoi(n - 1, temp, end, start)

print(2 ** s - 1)
if s < 21:
    hanoi(s, 1, 3, 2)

"""




