import sys
n = int(input())

nums = list(map(int, sys.stdin.readline().split()))

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

nums = merge_sort(nums)

m = int(input())

def exist(x):
    pl = 0
    pr = n - 1
    while pl <= pr:
        pc = (pl + pr) // 2
        if nums[pc] == x:
            return 1
        elif nums[pc] < x:
            pl = pc + 1
        else:
            pr = pc - 1

    return 0

cards = list(map(int, input().split()))
for i in cards:
    print(exist(i))