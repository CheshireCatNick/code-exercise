#include <iostream>
#include <map>
#include <string>

using namespace std;
int main(void) {
    int n;
    cin >> n;
    map<string, int> m;
    map<string, int>::iterator it;
    string t;
    for (int i = 0; i < n; i++) {
        cin >> t;
        it = m.find(t);
        if (it == m.end()) {
            m[t] = 1;
        }
        else {
            it->second++;
        }
    }
    int max = 0;
    for (it = m.begin(); it != m.end(); it++) {
        //cout << it->first << " " << it->second << '\n';
        max = it->second > max ? it->second : max;
    }
    for (it = m.begin(); it != m.end(); it++) {
        if (it->second == max) {
            cout << it->first << '\n';
        }
    }
}