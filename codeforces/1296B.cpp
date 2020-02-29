#include <iostream>

using namespace std;
int main(void) {
    int t;
    cin >> t;
    int s;
    while (t--) {
        cin >> s;
        int rest, spent, totalSpent = 0;
        while (s >= 10) {
            spent = s / 10 * 10;
            totalSpent += spent;
            s = s - spent + spent / 10;
        }
        cout << totalSpent + s << '\n';
    }
    return 0;
}