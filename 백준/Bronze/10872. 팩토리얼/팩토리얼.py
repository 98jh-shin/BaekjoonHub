import sys

s = int(sys.stdin.readline().strip())
result = 1
for i in range(1, s + 1):
    result *= i

print(result)