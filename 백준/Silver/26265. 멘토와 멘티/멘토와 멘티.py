import sys
n = int(input())

ment_list = [list(sys.stdin.readline().split()) for _ in range(n)]
ment_list.sort(key = lambda x: x[1], reverse = True)
ment_list.sort(key = lambda x: x[0])

for m in ment_list:
    print(*m)