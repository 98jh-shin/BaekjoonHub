#include <iostream>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;

  string str;
  for (int i = 0; i < t; ++i) {
    cin >> str;
    cout << str.front() << str.back() << '\n';
  }

  return 0;
}