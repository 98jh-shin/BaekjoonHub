import sys

N, K = map(int, sys.stdin.readline().split()) # 동전의 개수, 목표 금액

coins = []
for i in range(N):
    coins.append(int(sys.stdin.readline()))

count = 0
while coins: # 스택에 코인이 남았으면
    coin = coins.pop() # 일단 코인을 꺼내

    count += K // coin
    K %= coin

    if K == 0:
        break

print(count)