n = int(input())

if n < 3:
    print(n)
    exit()

dp_1 = 1 # dp 배열에 보관 x 변수에 저장
dp_2 = 1
tmp = 0
dp_3 = 2
for _ in range(2, (((n + 1) // 2) + 1)):
    tmp = dp_1
    dp_1 = dp_2
    dp_2 = dp_3
    dp_3 = (dp_1 + dp_2) % 15746

res = (dp_3 * dp_1) + (dp_2 * tmp)
print(res % 15746)



"""
1
1
2
3
5
8
13
19
34
55
89
144
233
377
610
"""