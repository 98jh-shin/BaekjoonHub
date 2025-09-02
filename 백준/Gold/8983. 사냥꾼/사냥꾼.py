import sys

m, n, l = map(int, sys.stdin.readline().split())

shooting = list(map(int, sys.stdin.readline().split()))

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

shooting = merge_sort(shooting)

animals = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bound(arr, target, rev):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if not rev:
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        else:
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
    return lo

count = 0
for anm_x, anm_y in animals:
    d = l - anm_y
    if d < 0:
        continue
    left = anm_x - d
    right = anm_x + d
    left_idx = bound(shooting, left, False)
    right_idx = bound(shooting, right, True)

    if right_idx > left_idx:
        count += 1

print(count)