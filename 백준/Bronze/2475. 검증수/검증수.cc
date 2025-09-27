#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n = 5;
  vector<int> numbers(n);

  for (int i = 0; i < n; ++i) {
    cin >> numbers[i];
  }

  int sum = 0;
  for (int num : numbers) {
    sum += num * num;
  }

  cout << sum % 10 << '\n';

  return 0;
}