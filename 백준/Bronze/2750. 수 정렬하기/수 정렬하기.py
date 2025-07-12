import sys

s = int(input())

num_list = [int(sys.stdin.readline().strip()) for _ in range(s)]


for i in range(s):
    min_index = i
    for j in range(i + 1, s):
        if num_list[j] < num_list[min_index]:
            min_index = j
    num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

for i in num_list:
    print(i)