import sys

n, k = map(int, sys.stdin.readline().split())

num_A = list(map(int, sys.stdin.readline().split()))
num_B = list(map(int, sys.stdin.readline().split()))

num_A.sort()
num_B.sort()

a = 0
b = 0
res = 0

while a < len(num_A) and b < len(num_B):
    if num_A[a] < num_B[b]:
        res += 1
        a += 1
    elif num_A[a] > num_B[b]:
        res += 1
        b += 1
    else:
        a += 1
        b += 1

res += (len(num_A) - a) + (len(num_B) - b)

print(res)