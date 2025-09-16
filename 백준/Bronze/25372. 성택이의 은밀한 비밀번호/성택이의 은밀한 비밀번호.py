import sys

n = int(sys.stdin.readline())

for _ in range(n):
    m = sys.stdin.readline().rstrip()
    length = len(m)
    if length > 9 or length < 6:
        print("no")
    else:
        print("yes")