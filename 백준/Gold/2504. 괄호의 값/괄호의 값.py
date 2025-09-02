import sys

def solve():
    s = sys.stdin.readline().rstrip()
    stack = []

    for c in s:
        if c in '([':
            stack.append(c)

        elif c in ')]':
            # 1) 빈 스택 체크
            if not stack:
                print(0)
                return

            # 2) 숫자 문자열 합산
            tmp = 0
            while stack and stack[-1].isdigit():
                tmp += int(stack.pop())

            # 3) 짝 여는 괄호·배수 결정
            pair = '(' if c == ')' else '['
            mul  = 2   if c == ')' else 3
            if not stack or stack[-1] != pair:
                print(0)
                return

            # 4) 여는 괄호 제거 후 결과 푸시
            stack.pop()
            stack.append(str(tmp * mul if tmp else mul))

        else:
            # 허용되지 않는 문자
            print(0)
            return

    # 남은 게 모두 숫자여야 최종 합산
    result = 0
    for x in stack:
        if not x.isdigit():
            print(0)
            return
        result += int(x)

    print(result)

if __name__ == "__main__":
    solve()
