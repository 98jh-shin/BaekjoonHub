n = int(input())

if n < 3:
    print(n)
    exit()

dp_1 = 1 # dp 배열에 보관 x 변수에 저장
dp_2 = 2
for _ in range(3, n + 1):
    tmp = dp_1
    dp_1 = dp_2
    dp_2 = (tmp + dp_1) % 15746

print(dp_2)

