#include <iostream>
#include <string>
// for memset
#include <string.h>
using namespace std;

int main()
{
    int t, pc[26], hc[26];
    cin >> t;
    while (t--) {
        string p, h;
        cin >> p >> h;
        if (h.length() < p.length()) {
            cout << "NO\n";
            continue;
        }
        memset(pc, 0, 26 * sizeof(int));
        memset(hc, 0, 26 * sizeof(int));
        for (int i = 0; i < p.length(); i++) {
            pc[p[i] - 'a']++;
        }
        bool isHash = false;
        for (int i = 0; i < h.length() - p.length() + 1; i++) {
            bool isPermu = false;
            for (int j = 0; j < 26; j++) {
                hc[j] = 0;
            }
            for (int j = 0; j < p.length(); j++) {
                hc[h[i + j] - 'a']++;
            }
            for (int j = 0; j < 26; j++) {
                if (hc[j] != pc[j]) break;
                else if (j == 25) isPermu = true;
            }
            if (isPermu) {
                isHash = true;
                break;
            }
        }
        if (isHash) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}