import sys

n = int(input())
arr = list(sys.stdin.readline().rstrip())

while True:
    remove_list = []
    for i in range(len(arr) - 2):
        if arr[i] == "P" and arr[i + 1] == "S" and arr[i + 2] in ["4", "5"]:
            remove_list.append(i + 2)

    if not remove_list:
        break

    for idx in reversed(remove_list):
        arr.pop(idx)

print("".join(arr))
