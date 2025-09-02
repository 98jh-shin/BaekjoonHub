import sys

sys.stdin = open('input.txt', 'r')

x, y = map(int, sys.stdin.readline().split())

s = int(sys.stdin.readline())

w_list = [0, y]
y_list = [0, x]

for c in range(s):
    dir, loc = map(int, sys.stdin.readline().split())

    if dir == 0:
        w_list.append(loc)
    if dir == 1:
        y_list.append(loc)


def sort_list(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

    return arr

w_list = sort_list(w_list)
y_list = sort_list(y_list)

w_max = 0
y_max = 0

for i in range(len(w_list) - 1):
    if w_max < w_list[i + 1] - w_list[i]:
        w_max = w_list[i + 1] - w_list[i]


for i in range(len(y_list) - 1):
    if y_max < y_list[i + 1] - y_list[i]:
        y_max = y_list[i + 1] - y_list[i]

print(w_max * y_max)