#include <iostream>

using namespace std;
long long sumToN(long long n) {
    return (n + 1) * n / 2;
}
int main(void) {
    int t; cin >> t;
    long long n, m;
    while (t--) {
        cin >> n >> m;
        long long total = sumToN(n);
        long long gNum = m + 1;
        long long z = n - m;
        long long zPerGroup = z / gNum;
        long long rest = z % gNum;
        cout << total - (gNum - rest) * sumToN(zPerGroup) - rest * sumToN(zPerGroup + 1) << '\n';
    }
    return 0;
}