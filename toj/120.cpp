// @topics: array interval sum
#include <stdio.h>

int main(void) {
    int treeNum;
    scanf("%d", &treeNum);
    int trees[treeNum];
    for (int i = 0; i < treeNum; i++) {
        scanf("%d", &trees[i]);
    }
    // preprocessing
    long long int sums[treeNum + 1];
    sums[0] = 0;
    for (int i = 1; i <= treeNum; i++) {
        sums[i] = sums[i - 1] + trees[i - 1];
    }
    // ans
    int customerNum;
    scanf("%d", &customerNum);
    for (int i = 0; i < customerNum; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        int start = (a < b) ? a : b;
        int end = (a > b) ? a : b;
        printf("%lld\n", sums[end] - sums[start - 1]);
    }
    return 0;
}