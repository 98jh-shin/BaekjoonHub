import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))


def quick_sort(arr, left, right):
    if left >= right:
        return

    mid = (right + left) // 2
    pivot = arr[mid]

    i = left
    j = right

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quick_sort(arr, left, j)
    quick_sort(arr, i, right)


quick_sort(arr, 0, n - 1)

best_sum = 10000000011

left = 0
right = n - 1
best_left = 0
best_right = 0

while left < right:
    sum = arr[left] + arr[right]
    if sum == 0:
        best_left = arr[left]
        best_right = arr[right]
        break
    if best_sum > abs(sum):
        best_sum = abs(sum)
        best_left = arr[left]
        best_right = arr[right]

    if sum < 0:
        left += 1
    else:
        right -= 1

print(best_left, best_right, sep=" ")