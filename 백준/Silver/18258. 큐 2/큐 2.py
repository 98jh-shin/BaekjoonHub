import sys

class queue:
    def __init__(self):
        self.queue = []
        self.head = 0
    def push(self, data):
        self.queue.append(data)
    def pop(self):
        if self.head < len(self.queue):
            tmp = self.queue[self.head]
            self.head += 1
            return tmp
        else:
            return -1
    def size(self):
        return len(self.queue) - self.head
    def empty(self):
        return 0 if self.head < len(self.queue) else 1
    def front(self):
        return self.queue[self.head] if self.head < len(self.queue) else -1
    def back(self):
        return self.queue[-1] if self.head < len(self.queue) else -1

n = int(input())
q = queue()
for _ in range(n):
    input = sys.stdin.readline().split()
    if input[0] == "push":
        q.push(input[1])
    elif input[0] == "pop":
        print(q.pop())
    elif input[0] == "size":
        print(q.size())
    elif input[0] == "empty":
        print(q.empty())
    elif input[0] == "front":
        print(q.front())
    elif input[0] == "back":
        print(q.back())