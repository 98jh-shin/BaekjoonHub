import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
m = int(input())
find_list = list(map(int, sys.stdin.readline().split()))


def heap(a, left, right):
    temp = a[left]

    parent = left
    while parent < (right + 1) // 2:
        cl = parent * 2 + 1
        cr = cl + 1
        if cr <= right and a[cr] > a[cl]:
            child = cr
        else:
            child = cl
        if temp >= a[child]:
            break
        a[parent] = a[child]
        parent = child
    a[parent] = temp


def heap_sort(a):
    for i in range((n - 1) // 2, -1, -1):
        heap(nums, i, n - 1)

    for end in range(n - 1, 0, - 1):
        a[0], a[end] = a[end], a[0]
        heap(a, 0, end - 1)


heap_sort(nums)


def exist(x):
    pl = 0
    pr = n - 1
    while pl <= pr:
        pc = (pl + pr) // 2
        if nums[pc] == x:
            return True
        elif nums[pc] < x:
            pl = pc + 1
        else:
            pr = pc - 1

    return False


for x in find_list:
    print("1" if exist(x) else "0")

