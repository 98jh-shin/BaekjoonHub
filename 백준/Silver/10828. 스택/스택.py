import sys


class stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop() if self.stack else -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 0 if self.stack else 1

    def top(self):
        return self.stack[-1] if self.stack else -1


n = int(input())
st = stack()

for _ in range(n):
    input = sys.stdin.readline().split()
    if input[0] == "push":
        st.push(input[1])
    elif input[0] == "pop":
        print(st.pop())
    elif input[0] == "size":
        print(st.size())
    elif input[0] == "empty":
        print(st.empty())
    elif input[0] == "top":
        print(st.top())
