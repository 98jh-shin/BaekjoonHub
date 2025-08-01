import sys

s = int(input())


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]):
            result.append(left[i])
            i += 1
        elif len(left[i]) > len(right[j]):
            result.append(right[j])
            j += 1
        else:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1


    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


word_list = [sys.stdin.readline().strip() for _ in range(s)]

word_list = merge_sort(word_list)

result = [word_list[0]]
for i in range(1, len(word_list)):
    if word_list[i] != word_list[i - 1]:
        result.append(word_list[i])

print(*(i for i in result))
