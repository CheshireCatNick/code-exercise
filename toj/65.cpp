#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void) {
    srand(clock());
    printf("%d\n", rand() % 2);
    return 0;
}
