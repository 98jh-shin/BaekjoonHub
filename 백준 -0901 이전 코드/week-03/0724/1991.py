import sys

sys.stdin = open('../../../input.txt', 'r')

n = int(input())

trees = {}
for _ in range(n):
    par, left, right = sys.stdin.readline().split()
    trees[par] = (left, right)


def preorder(t):
    if t == '.':
        return
    print(t, end='')
    preorder(trees[t][0])
    preorder(trees[t][1])


def inorder(t):
    if t == '.':
        return
    inorder(trees[t][0])
    print(t, end='')
    inorder(trees[t][1])


def postorder(t):
    if t == '.':
        return
    postorder(trees[t][0])
    postorder(trees[t][1])
    print(t, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')


