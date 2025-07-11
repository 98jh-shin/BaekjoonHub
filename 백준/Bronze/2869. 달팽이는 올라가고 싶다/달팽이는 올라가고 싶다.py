import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

hpd = a - b
count = math.ceil((v - a) / hpd)
result = count + 1

print(int(result))