import sys

sys.stdin = open('../../../input.txt', 'r')

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except ValueError:
        break