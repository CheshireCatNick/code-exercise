#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
    srand(time(NULL));
    puts("1");
    char lStr[1000001];
    for (int i = 0; i < 1000000; i++) {
        lStr[i] = 'a' + rand() % 26;
    }
    puts(lStr);
    puts("1000");
    for (int i = 0; i < 1000; i++) {
        int start = rand() % (1000000 - 55);
        for (int j = start; j < start + 50; j++) {
            printf("%c", lStr[j]);
        }
        puts("");
    }
}