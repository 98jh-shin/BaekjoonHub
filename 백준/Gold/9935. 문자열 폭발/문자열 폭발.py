import sys

txt = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []

for ch in txt:
    stack.append(ch)

    if len(stack) < len(bomb):
        continue
    else:
        if ch == bomb[-1]:
            temp = ''.join(stack[len(stack) - len(bomb):])
            if temp == bomb:
                for _ in range(len(bomb)):
                    stack.pop()
                    
if stack:
    print(''.join(stack))
else:
    print('FRULA')
