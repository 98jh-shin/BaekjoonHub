#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <map>

using namespace std;

void solve() {
    int k;
    cin >> k;

    priority_queue<int, vector<int>, less<>> max_heap;
    priority_queue<int, vector<int>, greater<>> min_heap;
    map<int, int> count;

    for (int i = 0; i < k; ++i) {
        char ch;
        int n;
        cin >> ch >> n;

        if (ch == 'I') {
            max_heap.push(n);
            min_heap.push(n);
            count[n]++;
        } else {
            if (n == 1) {
                // 비어있지 않고 현재 탑이 이미 지워낸 녀석인지 map을 통해 확인
                while (!max_heap.empty() && count[max_heap.top()] == 0) {
                    max_heap.pop();
                }
                if (!max_heap.empty()) {
                    count[max_heap.top()]--;
                    max_heap.pop();
                }
            } else {
                while (!min_heap.empty() && count[min_heap.top()] == 0) {
                    min_heap.pop();
                }
                if (!min_heap.empty()) {
                    count[min_heap.top()]--;
                    min_heap.pop();
                }
            }
        }
    }

    // 남은 찌꺼기 처리
    while (!max_heap.empty() && count[max_heap.top()] == 0) {
        max_heap.pop();
    }
    while (!min_heap.empty() && count[min_heap.top()] == 0) {
        min_heap.pop();
    }

    if (max_heap.empty() || min_heap.empty()) {
        cout << "EMPTY\n";
        return;
    } else {
        cout << max_heap.top() << " " << min_heap.top() << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}