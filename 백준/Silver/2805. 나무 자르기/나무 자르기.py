import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

hi = trees[0]
for t in trees:
    if hi < t:
        hi = t
lo = 0 
result = 0

while lo <= hi:
    mid = (lo + hi) // 2 
    total = 0
    for t in trees:
        if t > mid:
            total += t - mid
    
    if total >= m:
        result = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(result)
