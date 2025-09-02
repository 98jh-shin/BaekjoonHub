import sys

sys.stdin = open('input.txt', 'r')

input = list(sys.stdin.readline().split())

print(len(input))

print(len(sys.stdin.readline().split()))