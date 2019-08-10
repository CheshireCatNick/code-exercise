// @topics: inversion
// @note: not passed yet
#include <stdio.h>
#include <stdlib.h>

#define MAX 2000001

typedef struct number {
    int num;
    int index;
} Number;

int compare(const void* a, const void* b) {
    int na = ((Number*)a) -> num;
    int nb = ((Number*)b) -> num;
    return na - nb;
}

int main(void) {
    int n;
    scanf("%d", &n);
    Number numbers[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &numbers[i].num);
        numbers[i].index = i + 1;
    }
    qsort(numbers, n, sizeof(Number), compare);
    for (int i = 0; i < n; i++) {
        printf("%d %d\n", numbers[i].num, numbers[i].index);
    }
    int step = 0;
    for (int i = 0; i < n; i++) {
        step += abs(numbers[i].index - (i + 1));
    }
    printf("%d\n", step / 2);
    return 0;
}