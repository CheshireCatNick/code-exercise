#include <iostream>
#include <string>
using namespace std;
int main(void) {
    int t; cin >> t;
    string a, b, c;
    while (t--) {
        cin >> a >> b >> c;
        bool success = false;
        for (int i = 0; i < c.length(); i++) {
            if (a[i] != c[i] && b[i] != c[i]) break;
            if (i == c.length() - 1) success = true;
        }
        if (success) cout << "YES\n";
        else cout << "NO\n";
    }
}