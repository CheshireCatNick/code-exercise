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
#define ROF(i, a, b) for (int i = int(b) - 1; i >= a; i--)
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
typedef vector<LL> VL;

template<class T> void _R(T &x) { cin >> x; }
void _R(int &x) { scanf("%d", &x); }
void _R(double &x) { scanf("%lf", &x); }
void _R(char &x) { scanf(" %c", &x); }
void _R(char *x) { scanf("%s", x); }
void _R(LL &x) { scanf("%lld", &x); }
void R() {}
template<class T, class... U> void R(T &head, U &... tail) { _R(head); R(tail...); }
 
template<class T> void _W(const T &x) { cout << x; }
void _W(const int &x) { printf("%d", x); }
void _W(const double &x) { printf("%.16f", x); }
void _W(const char &x) { putchar(x); }
void _W(const char *x) { printf("%s", x); }
void _W(const LL &x) { printf("%lld", x); }
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

int main(void) {
    int n;
    R(n);
    if (n == 1) {
        puts("1");
        return 0;
    }
    if (n <= 3) {
        puts("NO SOLUTION");
        return 0;
    }
    int start = n - 2;
    if (n % 2 == 0) {
        start = n - 1;
    }
    while (start >= 1) {
        printf("%d ", start);
        start -= 2;
    }
    printf("%d ", n);
    start = 2;
    while (start <= n - 3) {
        printf("%d ", start);
        start += 2;
    }
    printf("%d\n", start);
	return 0;
}