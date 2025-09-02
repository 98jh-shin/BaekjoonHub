import sys

sys.stdin = open('../../../input.txt', 'r')

v, e = map(int, sys.stdin.readline().split())

edges = []
parent = [i for i in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

edges = merge_sort(edges)

def find(x):
    if x != parent[x]:
        x = parent[x]
    return x


def union(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root == b_root:
        return False
    parent[b_root] = a_root
    return True


total = 0
count = 0

for cost, a, b in edges:
    if union(a, b):
        total += cost
        count += 1
        if count == v - 1:
            break
print(total)

