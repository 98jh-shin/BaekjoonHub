import sys

n = int(sys.stdin.readline())

i = 2
while i * i <= n:
    if n % i == 0:
        print(i)
        n = n // i
    else:
        i += 1

if n > 1:
    print(n)