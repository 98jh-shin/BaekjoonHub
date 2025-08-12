import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
INF = sys.maxsize

G = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(cur, mask):
    if mask == (1 << N) - 1: # 모든 도시를 순환 했다면
        if G[cur][0] == 0: # 시작점으로 돌아갈 수 없다면
            return INF # 비용을 크게 줘서 이 방법 제외
        else:
            return G[cur][0] # 시작점으로 돌아가는 비용 리턴

    if dp[cur][mask] != -1: # 이미 방문한 도시라면
        return dp[cur][mask] # 바로 반환

    best = INF

    for nxt in range(N):
        if not (mask & (1 << nxt)) and G[cur][nxt]: # 마스크랑 and 연산이 0 (아직 방문 x), 배열값이 0이 아니면
            cost = G[cur][nxt] + tsp(nxt, (mask | (1 << nxt)))
            if best > cost:
                best = cost

    dp[cur][mask] = best
    return best

print(tsp(0, 1 << 0))



