import sys

n, w, h = map(int, sys.stdin.readline().split())
m = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
max = ((w ** 2) + (h ** 2)) ** 0.5

print("\n".join(["DA" if max >= i else "NE" for i in m]))
