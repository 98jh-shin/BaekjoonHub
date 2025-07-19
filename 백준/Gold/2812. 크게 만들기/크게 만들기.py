import sys
n, k = map(int, sys.stdin.readline().split())

arr = sys.stdin.readline().rstrip()
nums = []
count = 0

for ch in arr:
    tmp = int(ch)

    while nums and count < k and nums[-1] < tmp:
        nums.pop()
        count += 1

    nums.append(tmp)

while count < k and nums:
    nums.pop()
    count += 1

if nums:
    print("".join(str(num) for num in nums))
else:
    print(0)