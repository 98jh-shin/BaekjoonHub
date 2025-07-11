import sys

n = int(input())

for _ in range(n):
    temp = ""
    line = list(sys.stdin.readline().split())

    for i in line[1]:
        temp += i * int(line[0])
        
    print(temp)
