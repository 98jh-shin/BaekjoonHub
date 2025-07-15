import sys

sys.stdin = open('input.txt', 'r')
# 재귀함수로 풀어야한다.
# s = int(sys.stdin.readline().strip())
# result = 1
# for i in range(1, s + 1):
#     result *= i
#
# print(result)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(int(input())))