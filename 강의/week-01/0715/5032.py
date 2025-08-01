import sys

a, b ,c = map(int, sys.stdin.readline().split())

total = a + b
count = 0

while total >= c:
    new = total // c
    count += new
    total = total % c + new

print(count)