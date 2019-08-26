#include <stdio.h>
#include <string.h>
#define MAX_DIGIT 10000

// c = a + b
void sum(char* a, char* b, char* c) {
    int ap = strlen(a) - 1;
    int bp = strlen(b) - 1;
    int sum, carry = 0, digit = 0;
    while (ap >= 0 && bp >= 0) {
        sum = a[ap] - '0' + b[bp] - '0' + carry;
        carry = 0;
        if (sum >= 10) {
            sum %= 10;
            carry = 1;
        }
        c[digit] = '0' + sum;
        ap--;
        bp--;
        digit++;
    }
    if (ap == -1) {
        while (bp >= 0) {
            sum = carry + (b[bp] - '0');
            carry = 0;
            if (sum >= 10) {
                sum %= 10;
                carry = 1;
            }
            c[digit] = '0' + sum;
            digit++;
            bp--;
        }
    }
    else if (bp == -1) {
        while (ap >= 0) {
            sum = carry + (a[ap] - '0');
            carry = 0;
            if (sum >= 10) {
                sum %= 10;
                carry = 1;
            }
            c[digit] = '0' + sum;
            digit++;
            ap--;
        }
    }
    if (carry == 1) {
        c[digit] = '1';
        digit++;
    }
    char tmp;
    for (int i = 0; i <= digit / 2 - 1; i++) {
        tmp = c[i];
        c[i] = c[digit - i - 1];
        c[digit - i - 1] = tmp;
    }
    c[digit] = '\0';
    return;
}
int main(void) {
    int n;
    scanf("%d", &n);
    if (n == 0) {
        puts("0");
        return 0;
    }
    if (n == 1 || n == 2) {
        puts("1");
        return 0;
    }
    char a[MAX_DIGIT], b[MAX_DIGIT], c[MAX_DIGIT];
    strcpy(a, "1");
    strcpy(b, "1");
    for (int i = 3; i <= n; i++) {
        sum(a, b, c);
        strcpy(a, b);
        strcpy(b, c);
    }
    puts(c);
    return 0;
}