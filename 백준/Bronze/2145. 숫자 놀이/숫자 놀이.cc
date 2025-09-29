#include <iostream>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  string N;

  while (cin >> N) {
    if (N == "0") {
      break;
    }

    while (N.length() > 1) {
      int sum = 0;
      for (int i = 0; i < N.length(); ++i) {
        sum += (N[i] - '0');
      }

      N = to_string(sum);
    }

    cout << N << "\n";
  }


  return 0;
}