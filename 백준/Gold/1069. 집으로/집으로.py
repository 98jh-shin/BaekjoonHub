import sys

X, Y, D, T = map(int, sys.stdin.readline().split())
dist = (X ** 2 + Y ** 2) ** 0.5

if D <= T:
    print(dist)
else:
    result = []

    result.append(dist) # 그냥 걸었을 때

    jumps = dist // D # 점프 횟수

    if jumps > 0:
        remain_dist = dist % D
        result.append((jumps * T) + remain_dist) # 점프하고 남은 거리 걸었을 때

        result.append((jumps + 1) * T) # 목적지에서 점프거리만큼 떨어진 위치로 점프 후 점프
    else:
        if 2 * T >= T + (D - dist):
            result.append(T + (D - dist)) # 점프 후 되돌아오기
        else:
            result.append(2 * T) # 시작점에서부터 점프 2번

    print(min(result))