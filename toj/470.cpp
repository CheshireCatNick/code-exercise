/*
pick elements from an array s.t. they have the maximum sum
condition: elements picked cannot be adjacent
ex1: 1 3 1 3 2 => 6
ex2: 3 2 1 1 6 => 10
ex3: 1 3 4 3 2 5 3 => 11
ex4: 1 -2 -3 7 -1 -10 -20 => 8
*/
#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int main(void) {
    int dayNum, ppDay, pDay, e;
    int dp[2];
    while (scanf("%d", &dayNum) != EOF) {
        dp[0] = 0;
        dp[1] = 0;
        for (int i = 0; i < dayNum; i++) {
            scanf("%d", &e);
            ppDay = i % 2;
            if (ppDay == 0) pDay = 1;
            else pDay = 0;
            dp[ppDay] = max(dp[ppDay] + e, dp[pDay]);
        }
        printf("%d\n", dp[ppDay]);
    }
    return 0;
}