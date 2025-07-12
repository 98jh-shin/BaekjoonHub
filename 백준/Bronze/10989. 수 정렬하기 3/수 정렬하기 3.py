import sys

s = int(input())

f = [0] * 10001
for i in range(s):
    f[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for _ in range(f[i]):
        print(i)