import sys

n, x = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

print(' '.join(str(i) for i in arr if i < x))
