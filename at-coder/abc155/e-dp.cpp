#include <iostream>
#include <string>
using namespace std;

int min(int a, int b) { return (a < b) ? a : b; }
int main(void) {
    string n;
    cin >> n;
    int ans = 0;
    int l = n.length();
    // 0: total banknotes if I pay this digit
    // 1: total banknotes if I let the clerk return on this digit
    int dp[l][2];
    int dg = n[l - 1] - '0';
    dp[l - 1][0] = dg;
    dp[l - 1][1] = 10 - dg;
    for (int i = l - 2; i >= 0; i--) {
        dg = n[i] - '0';
        dp[i][0] = min(dg + dp[i + 1][0], dg + dp[i + 1][1] + 1);
        dp[i][1] = min(10 - dg + dp[i + 1][0], 10 - dg - 1 + dp[i + 1][1]);
    }
    ans = min(dp[0][0], dp[0][1] + 1);
    cout << ans << '\n';
    return 0;
}