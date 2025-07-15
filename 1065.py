import sys

sys.stdin = open('input.txt', 'r')

s = int(sys.stdin.readline().strip())

count = 0



for i in range(1, s+1):
    if i < 100:
        count += 1
        continue

    a = i // 100
    b = (i // 10) % 10
    c = i % 10

    if (a - b) == (b - c):
        count += 1

print(count)

