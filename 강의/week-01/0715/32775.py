import sys

a, b = map(int, sys.stdin.readline().split())

if a <= b:
    print("high speed rail")
else:
    print("flight")