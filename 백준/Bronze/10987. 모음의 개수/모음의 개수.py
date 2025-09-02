import sys

arr = sys.stdin.readline().rstrip()
find_ch = ["a", "e", "i", "o", "u"]

count = 0
for ch in find_ch:
    count += arr.count(ch)

print(count)