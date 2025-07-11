import sys
import math

s = int(input())

numbers = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(s):
    if numbers[i] == 1:
        continue
    for n in range(2, math.isqrt(numbers[i]) + 1):
        if numbers[i] % n == 0:
            break
    else:
        count += 1

print(count)


