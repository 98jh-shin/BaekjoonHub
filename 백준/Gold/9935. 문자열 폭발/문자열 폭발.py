import sys

arr = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []
bomb_len = len(bomb)

for ch in arr:
    stack.append(ch)

    if len(stack) >= bomb_len and ch == bomb[-1]:
        if stack[-bomb_len:] == list(bomb):
            for _ in range(bomb_len):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')