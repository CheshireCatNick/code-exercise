#include <stdio.h>
#define MAXN 200005

int main(void) {
    int q;
    int kids[MAXN], ans[MAXN];
    scanf("%d", &q);
    while (q--) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &kids[i]);
            ans[i] = 0;
        }
        int day, start, now;
        for (int i = 0; i < n; i++) {
            if (ans[i] != 0) continue;
            day = 1;
            now = kids[i] - 1;
            while (now != i) {
                day++;
                now = kids[now] - 1;
            }
            ans[i] = day;
            now = kids[i] - 1;
            while (now != i) {
                ans[now] = day;
                now = kids[now] - 1;
            }
        }
        printf("%d", ans[0]);
        for (int i = 1; i < n; i++) {
            printf(" %d", ans[i]);
        }
        puts("");
    }
    return 0;
}