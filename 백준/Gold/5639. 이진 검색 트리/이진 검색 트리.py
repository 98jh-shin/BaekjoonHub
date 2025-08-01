import sys

sys.setrecursionlimit(10 ** 6)

preorder = []

for line in sys.stdin:
    preorder.append(int(line))


def postorder(start, end):
    if start >= end:
        return

    root = preorder[start]
    idx = start + 1

    while idx < end and preorder[idx] < root:
        idx += 1

    postorder(start + 1, idx)
    postorder(idx, end)
    print(root)

postorder(0, len(preorder))
