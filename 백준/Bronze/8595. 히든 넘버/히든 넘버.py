import sys

n = int(sys.stdin.readline().rstrip())
k = sys.stdin.readline().rstrip()

current_num = ""
total = 0

for char in k:
    if char.isdigit():
        current_num += char
    else:
        if current_num:
            total += int(current_num)
            current_num = ""

if current_num:
    total += int(current_num)

print(total)
