import sys

total = 0
min = 100

for _ in range(4):
    score = int(sys.stdin.readline().rstrip())
    if score < min:
        min = score
    total += score
total -= min

min = 100
for _ in range(2):
    score = int(sys.stdin.readline().rstrip())
    if score < min:
        min = score
    total += score
total -= min
print(total)
    