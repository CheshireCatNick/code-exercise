#include <stdio.h>
#define MAX 100010
int arr[MAX];
// disjoint set
int parent[MAX];
long long int sum[MAX];

int makeSet(int i) {
    parent[i] = i;
    sum[i] = arr[i];
    return sum[i];
}
int find(int i) {
    if (parent[i] == -1) return -1;
    if (parent[i] == i) return i;
    return find(parent[i]);
}
long long int join(int i, int j) {
    int ip = find(i);
    int jp = find(j);
    parent[ip] = jp;
    sum[jp] += sum[ip];
    return sum[jp];
}

int main(void) {
    int n;
    scanf("%d", &n);
    int a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    int op[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &op[i]);
    }
    // init disjoint set
    for (int i = 0; i < n; i++) {
        parent[i] = -1;
    }
    long long int maxUntilNow = -1, maxThisRound, ans[n];
    // reversely process operation
    for (int i = n - 1; i >= 0; i--) {
        int index = op[i] - 1;
        maxThisRound = makeSet(index);
        if (index >= 1 && find(index - 1) != -1) {
            maxThisRound = join(index, index - 1);
        }
        if (index <= n - 2 && find(index + 1) != -1) {
            maxThisRound = join(index, index + 1);
        }
        maxUntilNow = (maxThisRound > maxUntilNow) ? maxThisRound : maxUntilNow;
        ans[i] = maxUntilNow;
    }
    for (int i = 0; i < n; i++) {
        printf("%lld\n", ans[i]);
    }
}