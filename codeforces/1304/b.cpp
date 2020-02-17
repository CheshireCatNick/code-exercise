#include <iostream>
#include <algorithm>
#include <string>
#include <string.h>
using namespace std;

bool isPair(string& a, string& b) {
    string t = b;
    reverse(t.begin(), t.end());
    return a == t;
}
bool isAxis(string &a) {
    int t = a.length() / 2 - 1;
    for (int i = 0; i <= t; i++) {
        if (a[i] != a[a.length() - 1 - i]) {
            return false;
        }
    }
    return true;
}
int main(void) {
    int n, m;
    cin >> n >> m;
    string allStr[n];
    for (int i = 0; i < n; i++) {
        cin >> allStr[i];
    }
    // 0, 1 or 2
    int isUsed[n];
    memset(isUsed, 0, n * sizeof(int));
    // find pairs
    for (int i = 0; i < n; i++) {
        if (isUsed[i] != 0) continue;
        for (int j = i + 1; j < n; j++) {
            if (isUsed[j] != 0) continue;
            if (isPair(allStr[i], allStr[j])) {
                isUsed[i] = 1;
                isUsed[j] = 2;
                break;
            }
        }
    }
    //for (int i = 0; i < n; i++) cout << isUsed[i] << '\n';
    // find axis if exist
    // create string
    string axis = "";
    for (int i = 0; i < n; i++) {
        if (isUsed[i] != 0) continue;
        if (isAxis(allStr[i])) {
            axis = allStr[i];
            break;
        }
    }
    string front = "";
    for (int i = 0; i < n; i++) {
        if (isUsed[i] == 1) {
            front += allStr[i];
        }
    }
    string ans = front;
    reverse(front.begin(), front.end());
    ans += axis + front;
    cout << ans.length() << '\n' << ans << '\n';
}