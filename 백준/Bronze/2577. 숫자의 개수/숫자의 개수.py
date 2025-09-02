import sys

# sys.stdin = open('input.txt', 'r')

num_a = int(sys.stdin.readline())
num_b = int(sys.stdin.readline())
num_c = int(sys.stdin.readline())

result = num_a * num_b * num_c

total_list = list(map(int, str(result)))
num_list = [0 for _ in range(10)]

for i in total_list:
    num_list[i] += 1

for i in num_list:
    print(i)