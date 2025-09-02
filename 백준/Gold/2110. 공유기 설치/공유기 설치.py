import sys

n, c = map(int, sys.stdin.readline().split())
home_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    result = []
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

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

home_list = merge_sort(home_list)

def can_install(d):
    count = 1
    last_pos = home_list[0]
    for x in home_list[1:]:
        if x - last_pos >= d:
            count += 1
            last_pos = x
    return count >= c

ans = 0
lo = 1
hi = home_list[-1] - home_list[0]

while lo <= hi:
    mid = (lo + hi) // 2

    if can_install(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1

print(ans)