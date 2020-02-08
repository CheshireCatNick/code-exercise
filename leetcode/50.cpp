#include <stdio.h>

double myPow(double x, int n) {
    if (n == -2147483648) return 1 / (myPow(x, -(n / 2)) * myPow(x, -(n / 2)));
    if (n < 0) return 1 / myPow(x, -n);
    double ans = 1;
    while (n > 0) {
        if ((n & 1) == 1) {
            ans *= x;
        }
        x *= x;
        n >>= 1;
    }
    return ans;
}
/* recursive
double myPow(double x, int n) {
    if (n == -2147483648) return 1 / (myPow(x, -(n / 2)) * myPow(x, -(n / 2)));
    if (n < 0) return 1 / myPow(x, -n);
    if (n == 0) return 1;
    int nextP = n / 2;
    if (n % 2 == 0) return myPow(x, nextP) * myPow(x, nextP);
    else return myPow(x, nextP) * myPow(x, nextP) * x;
}
*/
int main(void) {
    printf("%lf\n", myPow(3, 10));
    return 0;
}