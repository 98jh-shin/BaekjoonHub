#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N; // 입력 받을 변수
vector<vector<int>> S; // 능력치 보관할 배열
vector<bool> start_team(N); // 스타트팀 보관할 bool형 배열
int min_diff = 1e9; // 10억으로 설정

void cal_diff() {
    int score_start = 0;
    int score_link = 0;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (start_team[i] && start_team[j]) {
                score_start += S[i][j];
            } else if (!start_team[i] && !start_team[j]) {
                score_link += S[i][j];
            }
        }
    }

    const int diff = abs(score_start - score_link);
    if (diff < min_diff) {
        min_diff = diff;
    }
}

void find_min_difference(int index, int count) {
    if (count == N / 2) {
        cal_diff();
        return;
    }

    if (index == N) {
        return;
    }

    // 나를 포함하는 경우
    start_team[index] = true;
    find_min_difference(index + 1, count + 1);

    // 나를 포함하지 않는 경우
    start_team[index] = false;
    find_min_difference(index + 1, count);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;



    S.assign(N, vector<int>(N));
    start_team.assign(N, false);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> S[i][j];
        }
    }

    find_min_difference(0, 0);

    cout << min_diff;
}