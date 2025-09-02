#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = 200000000; // E(200,000) * max_cost(1,000) 보다 큰 값으로 설정

vector<pair<int, int>> adj[801];
int N, E;

// 시작점 start에서 다른 모든 정점까지의 최단 거리를 계산하는 다익스트라 함수
vector<int> dijkstra(int start) {
    vector<int> dist(N + 1, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    dist[start] = 0;
    pq.push({0, start}); // {비용, 정점}

    while (!pq.empty()) {
        int cost = pq.top().first;
        int here = pq.top().second;
        pq.pop();

        if (dist[here] < cost) {
            continue;
        }

        for (auto const& [there, weight] : adj[here]) {
            int next_cost = cost + weight;
            if (dist[there] > next_cost) {
                dist[there] = next_cost;
                pq.push({next_cost, there});
            }
        }
    }
    return dist;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> E;

    for (int i = 0; i < E; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        // 무방향 그래프이므로 양쪽으로 간선 추가
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    int v1, v2;
    cin >> v1 >> v2;

    // 1, v1, v2에서 시작하는 다익스트라 알고리즘 실행
    vector<int> dist_from_1 = dijkstra(1);
    vector<int> dist_from_v1 = dijkstra(v1);
    vector<int> dist_from_v2 = dijkstra(v2);

    // 경로 1: 1 -> v1 -> v2 -> N
    // 오버플로우 방지를 위해 long long 사용
    long long path1 = (long long)dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N];

    // 경로 2: 1 -> v2 -> v1 -> N
    long long path2 = (long long)dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N];

    long long answer = min(path1, path2);

    // 두 경로 모두 불가능한 경우(INF 이상) -1 출력
    if (answer >= INF) {
        cout << -1 << "\n";
    } else {
        cout << answer << "\n";
    }

    return 0;
}