#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  vector<int> step(4);
  for (int i = 0; i < 4; i++) {
    cin >> step[i];
  }

  sort(step.begin(), step.end());

  int result = step[0] * step[2];

  cout << result;


  return 0;
}