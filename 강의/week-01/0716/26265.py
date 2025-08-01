import sys

sys.stdin = open('../../../input.txt', 'r')

n = int(input())

ment_list = [sys.stdin.readline().split() for _ in range(n)]


def quick_sort(arr, left, right, idx, rev):
    if left >= right:
        return

    pivot = arr[(left + right) // 2][idx]
    i, j = left, right

    while i <= j:
        if not rev:
            while arr[i][idx] < pivot:
                i += 1
            while arr[j][idx] > pivot:
                j -= 1
        else:
            while arr[i][idx] > pivot:
                i += 1
            while arr[j][idx] < pivot:
                j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quick_sort(arr, left, j, idx, rev)
    quick_sort(arr, i, right, idx, rev)


quick_sort(ment_list, 0, n - 1, 0, False)

count = 0
while count < n:
    tmp = 0
    for i in range(count, n):
        if ment_list[i][0] == ment_list[count][0]:
            tmp += 1
        else:
            break
    quick_sort(ment_list, count, count + tmp - 1, 1, True)
    count += tmp

for line in range(n):
    print(" ".join(ment_list[line]))