#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    // 스택 1, 문자열 1, int 3
    string str;
    stack<int> s;
    int index = 1;
    int i = 0;
    int x;

    while (i < n) {
        cin >> x;

        while (x >= index) {
            str += "+\n";
            s.push(index++);
        }

        if (s.top() == x) {
            str += "-\n";
            s.pop();
            ++i;
        } else {
            cout << "NO\n";
            return 0;
        }
    }

    cout << str;
    return 0;
}