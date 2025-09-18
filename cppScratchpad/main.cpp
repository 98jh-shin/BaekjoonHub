#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int A, B;
        cin >> A >> B;
        cout << "Case #" << i + 1 << ": " << A << " + " << B << " = " << A + B << "\n";
    }

    return 0;
}