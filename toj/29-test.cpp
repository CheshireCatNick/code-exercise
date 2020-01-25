#include <stdio.h>
#include <string.h>
#include <vector>
#define M 1000010
#define N 50
#define ALPH 26
char lStr[M];
char keyword[N + 10];

using namespace std;
int main(void) {
    int t, q;
    scanf("%d", &t);
    while (t--) {
        scanf("%s", lStr);
        int l = strlen(lStr);
        vector<int> index[ALPH];
        for (int i = 0; i < l; i++) {
            index[lStr[i] - 'a'].push_back(i);
        }
        scanf("%d", &q);
        bool isSubstring;
        int kl, c, s, start, end;
        while (q--) {
            scanf("%s", keyword);
            kl = strlen(keyword);
            c = keyword[0] - 'a';
            s = (int)index[c].size();
            for (int i = 0; i < s; i++) {
                start = index[c][i];
                end = start + kl;
                if (end >= l) {
                    isSubstring = false;
                    break;
                }
                isSubstring = true;
                for (int j = start; j < end; j++) {
                    if (lStr[j] != keyword[j - start]) {
                        isSubstring = false;
                        break;
                    }
                }
                if (isSubstring) {
                    break;
                }
            }
            if (isSubstring) puts("y");
            else puts("n");
        }
    }
}