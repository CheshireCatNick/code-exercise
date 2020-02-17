#include <iostream>
using namespace std;

// return value in a
void un(int *a, int *b) {
    a[0] = (a[0] < b[0]) ? a[0] : b[0];
    a[1] = (a[1] > b[1]) ? a[1] : b[1];
}
void intersect(int *a, int *b) {
    a[0] = (a[0] > b[0]) ? a[0] : b[0];
    a[1] = (a[1] < b[1]) ? a[1] : b[1];
}
int main(void) {
    int t, m, n;
    cin >> t;
    int c[105][3];
    while (t--) {
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            cin >> c[i][0] >> c[i][1] >> c[i][2];
        }
        int range[] = {m, m};
        int range1[2], range2[2], cRange[2];
        int time = 0, timePassed;
        bool fail = false;
        for (int i = 0; i < n; i++) {
            timePassed = c[i][0] - time;
            range1[0] = range[0] - timePassed;
            range1[1] = range[0] + timePassed;
            range2[0] = range[1] - timePassed;
            range2[1] = range[1] + timePassed;
            un(range1, range2);
            cRange[0] = c[i][1];
            cRange[1] = c[i][2];
            intersect(range1, cRange);
            if (range1[0] > range1[1]) {
                fail = true;
                break;
            }
            range[0] = range1[0];
            range[1] = range1[1];
            time = c[i][0];
        }
        if (fail) cout << "NO\n";
        else cout << "YES\n";
    }
}