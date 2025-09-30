#include <iostream>
#include <map>
#include <cctype>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  map<char, pair<int, int>> pos;

  for (int i = 0; i < 4; ++i) {
    string str;
    cin >> str;
    for (int j = 0; j < 10; ++j) {
      pos[str[j]] = {i, j};
    }
  }

  string shotgun;
  cin >> shotgun;

  int minRow = 4;
  int minCol = 10;
  int maxRow = -1;
  int maxCol = -1;

  for (char c : shotgun) {
    int row = pos[c].first;
    int col = pos[c].second;
    minRow = min(minRow, row);
    maxRow = max(maxRow, row);
    minCol = min(minCol, col);
    maxCol = max(maxCol, col);
  }

  int midRow = minRow + 1;
  int midCol = minCol + 1;

  for (char c : shotgun) {
    if (pos[c].first == midRow && pos[c].second == midCol) {
      cout << c << endl;
    }
  }


  return 0;
}