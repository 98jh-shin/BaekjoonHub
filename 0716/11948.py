import sys

def sum_except_min(num_list):
    return sum(num_list) - min(num_list)

science = [int(sys.stdin.readline().rstrip()) for _ in range(4)]
social = [int(sys.stdin.readline().rstrip()) for _ in range(2)]

print(sum_except_min(science) + (sum_except_min(social)))