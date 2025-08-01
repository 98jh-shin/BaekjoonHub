import sys

sys.stdin = open('../../../input.txt', 'r')

input = sys.stdin.readline().strip()
arr = []
for ch in input:

    if ch == '(':
        arr.append(ch)
    elif ch == '[':
        arr.append(ch)
    elif ch == ')':
        if not arr:
            print(0)
            exit()
        prev = arr.pop()
        tmp = 0
        while prev.isdigit():
            tmp += int(prev)
            if not arr:
                print(0)
                exit()
            prev = arr.pop()

        if prev == '(':
            if tmp == 0:
                arr.append("2")
            else:
                arr.append(str(tmp * 2))
        else:
            print(0)
            exit()
    elif ch == ']':
        if not arr:
            print(0)
            exit()
        prev = arr.pop()
        tmp = 0
        while prev.isdigit():
            tmp += int(prev)
            if not arr:
                print(0)
                exit()
            prev = arr.pop()

        if prev == '[':
            if tmp == 0:
                arr.append("3")
            else:
                arr.append(str(tmp * 3))
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()
res = 0
for i in arr:
    if i == '(' or i == '[' or i == ')' or i == ']':
        print(0)
        exit()
    res += int(i)
print(res)
