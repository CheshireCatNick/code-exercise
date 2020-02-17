#include <iostream>
#include <string>
using namespace std;

int main(void) {
    string n;
    cin >> n;
    int ans = 0, carry = 0;
    for (int i = n.length() - 1; i >= 0; i--) {
        int dg = n[i] - '0';
        dg += carry;
        if (dg < 5) {
            // I'll pay this
            ans += dg;
            carry = 0;
        }
        else if (dg == 5) {
            int ndg = (i == 0) ? carry : n[i - 1] - '0';
            if (ndg < 5) {
                // I'll pay this
                ans += 5;
                carry = 0;
            }
            else {
                // I should make clerk return
                ans += 5;
                carry = 1;
            }
        }
        else {
            // I should make clerk return
            ans += 10 - dg;
            carry = 1;
        }
    }
    ans += carry;
    cout << ans << '\n';
    return 0;
}