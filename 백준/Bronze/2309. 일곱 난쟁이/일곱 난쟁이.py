import sys

num_list = [int(sys.stdin.readline().rstrip()) for _ in range(9)]

total = sum(num_list)

find = False
find_a = 0
find_b = 0


for i in range(9):
    for j in range(i + 1, 9):
        temp = num_list[i] + num_list[j]
        if total - temp == 100:
            find_a = i
            find_b = j
            find = True
            break
    if find:
        break

num_list.pop(find_b)
num_list.pop(find_a)

num_list.sort()
print(*(i for i in num_list))