import sys

n = int(sys.stdin.readline())

dig = len(str(n))

start = max(1, n - (dig * 9))
for i in range(start, n):
    if i + sum(int(k) for k in str(i)) == n:
        print(i)
        break
else:
    print(0)