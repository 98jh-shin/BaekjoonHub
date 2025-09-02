#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> graph[501];
vector<bool> visited;

bool bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = true;

    int node_cnt = 0;
    int edge_cnt = 0;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        node_cnt++;
        for (int next : graph[cur]) {
            edge_cnt++;
            if (!visited[next]) {
                q.push(next);
                visited[next] = true;
            }
        }
    }
    return (node_cnt - 1) == (edge_cnt / 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int test_count = 1;
    while (true) {
        int n, m;
        cin >> n >> m;
        if (n == 0 && m == 0) break;

        for (int i = 1; i < n + 1; i++) {
            graph[i].clear();
        }
        visited.assign(n + 1, false);

        for (int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }

        int tree_cnt = 0;
        for (int i = 1; i < n + 1; i++) {
            if (!visited[i]) {
                tree_cnt += bfs(i);
            }
        }

        if (tree_cnt == 0) {
            cout << "Case " << test_count << ": No trees.\n";
        } else if (tree_cnt == 1) {
            cout << "Case " << test_count << ": There is one tree.\n";
        } else {
            cout << "Case " << test_count << ": A forest of " << tree_cnt << " trees.\n";
        }
        test_count++;
    }
    return 0;
}