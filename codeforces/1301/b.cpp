#include <iostream>
#include <vector>

using namespace std;
int abs(int n) { return (n >= 0) ? n : -n; }
int main(void) {
    int t; cin >> t;
    int l, arr[4 * 100000 + 5];
    while (t--) {
        cin >> l;
        vector<int> v;
        for (int i = 0; i < l; i++) {
            cin >> arr[i];
        }
        if (arr[0] == -1 && arr[1] != -1) v.push_back(arr[1]);
        if (arr[l - 1] == -1 && arr[l - 2] != -1) v.push_back(arr[l - 2]);
        for (int i = 1; i < l - 1; i++) {
            if (arr[i] == -1) {
                if (arr[i - 1] != -1) v.push_back(arr[i - 1]);
                if (arr[i + 1] != -1) v.push_back(arr[i + 1]);
            }
        }
        if (v.size() == 0) {
            cout << "0 0\n";
            continue;
        }
        //for (int i = 0; i < v.size(); i++) {
        //    cout << v[i] << '\n';
        //}
        int min = v[0], max = v[0];
        for (int i = 1; i < v.size(); i++) {
            min = (v[i] < min) ? v[i] : min;
            max = (v[i] > max) ? v[i] : max;
        }
        int m = (min + max) / 2;
        int diff;
        max = -1;
        if (arr[0] == -1) arr[0] = m;
        for (int i = 0; i < l - 1; i++) {
            if (arr[i + 1] == -1) arr[i + 1] = m;
            diff = abs(arr[i + 1] - arr[i]);
            //cout << diff << ' ' << arr[i + 1] << ' ' << arr[i] << '\n';
            max = (diff > max) ? diff : max;
        }
        cout << max << ' ' << m << '\n';
    }
    return 0;
}