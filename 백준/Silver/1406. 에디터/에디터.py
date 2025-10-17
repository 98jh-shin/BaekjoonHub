import sys

arr = sys.stdin.readline().rstrip()

n = int(sys.stdin.readline())

left = []
right = []

left.extend(arr)

cursor = len(arr)

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'P':
        left.append(command[1])
    elif command[0] == 'B':
        if left:
            left.pop()

result = ''.join(left + right[::-1])
print(result)