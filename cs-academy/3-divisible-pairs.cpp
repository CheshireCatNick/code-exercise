#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    long long int counts[3];
    int number;
    for (int i = 0; i < 3; i++) counts[i] = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d", &number);
        counts[number % 3]++;
    }
    long long int ans = (counts[0] * (counts[0] - 1)) / 2;
    ans += counts[1] * counts[2];
    printf("%lld\n", ans);
}