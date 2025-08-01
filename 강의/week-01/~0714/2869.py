import sys
import math

sys.stdin = open('input.txt', 'r')

a, b, v = map(int, sys.stdin.readline().split())

# hpd = a - b
# count = math.ceil((v - a) / hpd)
# result = count + 1
#

result = (v - b - 1) // (a - b) + 1


print(int(result))