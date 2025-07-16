import sys

n = int(input())
words = {sys.stdin.readline().strip() for _ in range(n)}
answer = sorted(words, key=lambda w: (len(w), w))
print(*answer, sep="\n")