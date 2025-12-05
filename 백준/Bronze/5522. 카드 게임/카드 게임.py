import sys

total = 0

while True:

    line = sys.stdin.readline().rstrip()
    if not line:
        break

    total += int(line.rstrip())

print(total)