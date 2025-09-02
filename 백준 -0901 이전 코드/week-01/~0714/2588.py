import sys
sys.stdin = open('input.txt', 'r')

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

sum_A = a * (b % 10)
sum_B = a * ((b // 10) % 10)
sum_C = a * (b // 100)

print(sum_A)
print(sum_B)
print(sum_C)
print(sum_A + (sum_B * 10) + (sum_C * 100))