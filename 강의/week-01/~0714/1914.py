import sys
sys.stdin = open('input.txt', 'r')

s = int(input())

def hanoi(n, start, end, temp):
    if n > 20:
        return
    elif n == 1:
        print(start, end)
        return
    elif n > 1:
        hanoi(n - 1, start, temp, end)
        print(start, end)
        hanoi(n - 1, temp, end, start)

print(2 ** s - 1)
if s < 21:
    hanoi(s, 1, 3, 2)

