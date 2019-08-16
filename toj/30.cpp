#include <iostream>
#include <stdio.h>
#define MAX 1000001
using namespace std;

bool isPrime[MAX];
int count[MAX];

int main(void)
{
    // init
    for (int i = 0; i < MAX; i++) {
        isPrime[i] = true;
    }
    isPrime[0] = false;
    isPrime[1] = false;
    // remove non-prime
    for (int i = 2; i <= MAX / 2; i++) {
        if (!isPrime[i]) continue;
        int maxMul = MAX / i;
        for (int j = 2; j <= maxMul; j++) {
            isPrime[i * j] = false;
        }
    }
    // count
    int c = 0;
    for (int i = 0; i < MAX; i++) {
        if (isPrime[i]) c++;
        count[i] = c;
    }
    // ans
    int n;
    while (cin >> n) cout << count[n] << "\n";
	return 0;
}


