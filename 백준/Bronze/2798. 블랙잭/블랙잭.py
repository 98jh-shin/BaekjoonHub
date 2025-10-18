import sys

n, m = map(int,sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

total = 0

max_sum = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            card_sum = cards[i] + cards[j] + cards[k]

            if card_sum <= m:
                max_sum = max(max_sum, card_sum)

print(max_sum)