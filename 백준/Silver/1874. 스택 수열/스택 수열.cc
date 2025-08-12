#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    stack<int> s; // 인덱스를 보관할 스택
    int n; // 입력을 받을 n
    cin >> n; // 수열을 이루는 정수
    int index = 1; // 스택에 넣어줄 인덱스
    string str = "";

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        while (x >= index) {
            str += "+\n";
            s.push(index++);
        }

        if (s.empty() || s.top() < x) {
            cout << "NO\n";
            return 0;
        }

        while (!s.empty() && s.top() != x) {
            str += "-\n";
            s.pop();
        }

        str += "-\n";\
        s.pop();
    }

    cout << str;

    return 0;
}