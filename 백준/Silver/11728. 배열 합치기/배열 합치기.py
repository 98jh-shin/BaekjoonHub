import sys

n, k = map(int, sys.stdin.readline().split())

num_A = list(map(int, sys.stdin.readline().split()))
num_B = list(map(int, sys.stdin.readline().split()))

num_A.sort()
num_B.sort()

a = 0
b = 0
result = []

while a < len(num_A) and b < len(num_B):
    if num_A[a] < num_B[b]:
        result.append(num_A[a])
        a += 1
    elif num_A[a] > num_B[b]:
        result.append(num_B[b])
        b += 1
    else:
        result.append(num_A[a])
        result.append(num_B[b])
        a += 1
        b += 1

if a < len(num_A):
    result.extend(num_A[a:])
if b < len(num_B):
    result.extend(num_B[b:])

print(*result)