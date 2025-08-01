import sys

a, b = map(int, sys.stdin.readline().split())

num_list = []
for i in range(1, b + 1):
    tmp = a * i
    num_list.append(int(str(tmp)[::-1]))

# reversed_nums = [int(str(a * i)[::-1]) for i in range(1, b + 1)]

print(max(num_list))
