import sys

sys.stdin = open('input.txt', 'r')

s = int(input())

def merge(num_list):
    if len(num_list) == 1:
        return num_list
    mid = len(num_list) // 2
    left = merge(num_list[:mid])
    right = merge(num_list[mid:])

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

num_list = [int(sys.stdin.readline()) for _ in range(s)]
result = merge(num_list)
for i in result:
    print(i)