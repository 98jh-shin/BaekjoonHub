import sys

arr = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []

for ch in arr:
    stack.append(ch)

    if len(stack) < len(bomb):
        continue

    if ch == bomb[-1]:
        if stack[-len(bomb):] == list(bomb):
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')