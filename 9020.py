import sys
import math

sys.stdin = open('input.txt', 'r')

s = int(input())

def decimal(a, b):
    for n in range(2, math.isqrt(b) + 1):
        if a % n == 0 or b % n == 0:
            return False
    return True

for i in range(s):
    n = int(sys.stdin.readline())

    num_a = n // 2
    num_b = n // 2

    while True:
        if decimal(num_a, num_b):
            print(num_a, num_b)
            break
        num_a -= 1
        num_b += 1





