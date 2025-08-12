#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    stack<int> s; // 인덱스를 보관할 스택
    int n; // 입력을 받을 n
    cin >> n; // 수열을 이루는 정수
    int index = 1; // 스택에 넣어줄 인덱스
    string str = "";

    bool success = true;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        while (x >= index) {
            str += "+\n";
            s.push(index++);
        }

        if (s.top() == x) {
            str += "-\n";
            s.pop();
        } else {
            success = false;
            break;
        }
    }
    
    if (success) {
        cout << str;
    } else {
        cout << "NO\n";
    }
    return 0;
}