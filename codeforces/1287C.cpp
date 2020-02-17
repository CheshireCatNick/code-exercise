#include <iostream>
#include <vector>
#include <algorithm>
#define EVEN 0
#define ODD 1
using namespace std;

typedef struct interval {
    int l, r, type;
    interval(int l, int r, int t) : l(l), r(r), type(t){}
} Interval;
bool compareInterval(Interval a, Interval b) {
    return a.r - a.l < b.r - b.l;
}
bool isEven(int n) { return n % 2 == 0; }
bool isOdd(int n) { return !isEven(n); }
int main(void) {
    int n;
    cin >> n;
    int p[n];
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }
    // calculate available even number(0) and odd number(1)
    int a[2];
    a[EVEN] = n / 2;
    a[ODD] = a[0] + n % 2;
    for (int i = 0; i < n; i++) {
        if (p[i] != 0) a[p[i] % 2]--;
    }
    // skip start 0 and end 0;
    int s, e;
    for (s = 0; s < n && p[s] == 0; s++);
    if (s == n) {
        // all zero
        if (n == 1) cout << "0\n";
        else cout << "1\n";
        return 0;
    }
    for (e = n - 1; e >= 0 && p[e] == 0; e--);
    // create intervals and calculate complexity except interval
    int com = 0;
    vector<Interval> intervals;
    for (int i = s; i < e; i++) {
        int j;
        for (j = i + 1; p[j] == 0; j++);
        if (j - i == 1) {
            if (isEven(p[i]) != isEven(p[j])) com++;
            continue;
        }
        if (isEven(p[i]) && isEven(p[j])) {
            intervals.emplace_back(i, j, 0);
        }
        else if (isOdd(p[i]) && isOdd(p[j])) {
            intervals.emplace_back(i, j, 1);
        }
        else {
            // one odd one even
            com++;
        }
        i = j - 1;
    }
    sort(intervals.begin(), intervals.end(), compareInterval);
    int need;
    for (auto i : intervals) {
        //cout << i.l << " " << i.r << '\n';
        need = i.r - i.l - 1;
        if (isEven(i.type)) {
            if (a[EVEN] >= need) a[EVEN] -= need;
            else com += 2;
        }
        else {
            if (a[ODD] >= need) a[ODD] -= need;
            else com += 2;
        }
    }
    //cout << "com == " << com << '\n';
    // calculate start and end
    need = s;
    if (isEven(p[s])) {
        if (need <= a[EVEN]) a[EVEN] -= need;
        else com++;
    }
    else {
        if (need <= a[ODD]) a[ODD] -= need;
        else com++;
    }
    need = n - e - 1;
    if (isEven(p[e])) {
        if (need <= a[EVEN]) a[EVEN] -= need;
        else com++;
    }
    else {
        if (need <= a[ODD]) a[ODD] -= need;
        else com++;
    }
    cout << com << '\n';
    return 0;
}