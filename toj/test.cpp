#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
    srand(time(NULL));
    for (int i = 0; i < 1000000; i++) {
        printf("%c", 'a' + rand() % 26);
    }
    puts("");
}