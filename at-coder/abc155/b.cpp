#include <iostream>

using namespace std;
int main(void) {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    bool passed = true;
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) {
            if (a[i] % 3 != 0 && a[i] % 5 != 0) {
                passed = false;
                break;
            }
        }
    }
    if (passed) cout << "APPROVED\n";
    else cout << "DENIED\n";
}