// Nicky's template
// C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <inttypes.h>
// C++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <utility>

using namespace std;

#define FORN(i, n) for (int i = 0; i < int(n); i++)
#define NORF(i, n) for (int i = n - 1; i >= 0; i--)
#define FOR(i, a, b) for (int i = a; i < int(b); i++)
#define ROF(i, a, b) for (int i = int(b) - 1; i <= a; i--)
#define FORX(it, x) for (auto it = x.begin(); it != x.end(); it++)
#define FORS(i, s) for (int i = 0; s[i]; i++)
#define MS0(x) memset((x), 0, sizeof((x)))
#define MS1(x) memset((x), -1, sizeof((x)))
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) begin(x), end(x)

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class T> void _R(T &x) { cin >> x; }
void _R(int &x) { scanf("%d", &x); }
void _R(int64_t &x) { scanf("%" SCNd64, &x); }
void _R(double &x) { scanf("%lf", &x); }
void _R(char &x) { scanf(" %c", &x); }
void _R(char *x) { scanf("%s", x); }
void R() {}
template<class T, class... U> void R(T &head, U &... tail) { _R(head); R(tail...); }
 
template<class T> void _W(const T &x) { cout << x; }
void _W(const int &x) { printf("%d", x); }
void _W(const int64_t &x) { printf("%" PRId64, x); }
void _W(const double &x) { printf("%.16f", x); }
void _W(const char &x) { putchar(x); }
void _W(const char *x) { printf("%s", x); }
// print array
void WA(const int *a, int n) { for (int i = 0; i < n; _W(a[i++])) if (i != 0) putchar(' '); puts(""); }
template<class T> void _W(const vector<T> &x) { for (auto i = x.begin(); i != x.end(); _W(*i++)) if (i != x.cbegin()) putchar(' '); }
void W() {}
template<class T, class... U> void W(const T &head, const U &... tail) { _W(head); putchar(sizeof...(tail) ? ' ' : '\n'); W(tail...); }

template<class Iter> ostream &_out(ostream &s, Iter b, Iter e) {
    s << "[";
    for (auto it = b; it != e; it++) s << (it == b ? "" : " ") << *it;
    return s << "]";
}
template<class A, class B> ostream &operator<<(ostream &s, const pair<A, B> &p) { return s << "(" << p.first << ", " << p.second << ")"; }
template<class T> ostream &operator<<(ostream &s, const vector<T> &c) { return _out(s, ALL(c)); }
template<class T, size_t N> ostream &operator<<(ostream &s, const array<T, N> &c) { return _out(s, ALL(c)); }
template<class T> ostream &operator<<(ostream &s, const set<T> &c) { return _out(s, ALL(c)); }
template<class A, class B> ostream &operator<<(ostream &s, const map<A, B> &c) { return _out(s, ALL(c)); }

template<class T, class F = less<T>> void sort_uniq(vector<T> &v, F f = F()) { sort(begin(v), end(v), f); v.resize(unique(begin(v), end(v)) - begin(v)); }
template<class T> inline T bit(T x, int i) { return (x >> i) & 1; }
template<class T> inline bool chmax(T &a, const T &b) { return b > a ? a = b, true : false; }
template<class T> inline bool chmin(T &a, const T &b) { return b < a ? a = b, true : false; }
template<class T> using MaxHeap = priority_queue<T>;
template<class T> using MinHeap = priority_queue<T, vector<T>, greater<T>>;

template<class T> void _dump(const char *s, T &&head) { cerr << s << "=" << head << endl; }
template<class T, class... Args> void _dump(const char *s, T &&head, Args &&... tail) {
    for (int c = 0; *s != ',' || c != 0; cerr << *s++) {
        if (*s == '(' || *s == '[' || *s == '{') c++;
        if (*s == ')' || *s == ']' || *s == '}') c--;
    }
    cerr << "=" << head << ",";
    _dump(s + 1, tail...);
}
#define dump(...) do { fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); _dump(#__VA_ARGS__, __VA_ARGS__); } while (0)
double dp[305][305][305];
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
    int n;
    R(n);
    int a;
    int fs[] = {0, 0, 0};
    FORN(i, n) {
        R(a);
        fs[a - 1]++;
    }
    double tmp;
    double z;
    dp[0][0][0] = 0;
    int maxI = fs[0] + fs[1] + fs[2];
    int maxJ = fs[1] + fs[2];
    int maxK = fs[2];
    FORN(k, maxK + 1) FORN(j, maxJ + 1) FORN(i, maxI + 1) {
        if (i == 0 && j == 0 && k == 0) continue;
        tmp = 0;
        z = n - i - j - k;
        if (z < 0) break;
        if (i >= 1) tmp += i * dp[i - 1][j][k];
        if (j >= 1) tmp += j * dp[i + 1][j - 1][k];
        if (k >= 1) tmp += k * dp[i][j + 1][k - 1];
        //W(tmp);
        tmp /= n;
        tmp += 1;
        dp[i][j][k] = tmp / (1 - z / n);
        //W(dp[i][j][k]);
    }
    W(dp[fs[0]][fs[1]][fs[2]]);
    return 0;
}