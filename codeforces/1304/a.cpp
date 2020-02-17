#include <iostream>
using namespace std;

int main(void) {
    int t, x, y, a, b;
    cin >> t;
    while (t--) {
        cin >> x >> y >> a >> b;
        int d = y - x;
        int s = a + b;
        if (d % s == 0) {
            cout << d / s << '\n';
        }
        else cout << "-1\n";
    }
    return 0;
}