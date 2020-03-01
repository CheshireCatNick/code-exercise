// disjoint set union implemented by array
#include <stdio.h>

#define MAX 100005
int parent[MAX];
int sz[MAX];
void init() {
    for (int i = 0; i < MAX; i++) {
        parent[i] = -1;
        sz[i] = 0;
    }
}
void makeSet(int a) {
    parent[a] = a;
    sz[a] = 1;
}
int find(int a) {
    if (parent[a] == -1) return -1;
    if (parent[a] == a) return a;
    int p = find(parent[a]);
    parent[a] = p;
    return p;
}
void uni(int a, int b) {
    int pa = find(a);
    int pb = find(b);
    if (pa == -1 || pb == -1) return;
    if (pa == pb) return;
    // make pb a smaller one
    if (sz[pa] < sz[pb]) {
        int temp = pa;
        pa = pb;
        pb = temp;
    }
    // merge a smaller one into a larger one
    parent[pb] = pa;
    sz[pa] += sz[pb];
}
int getSize(int a) {
    return sz[find(a)];
}
int main(void) {
    init();
    makeSet(1);
    makeSet(2);
    makeSet(3);
    printf("%d\n", find(1));
    printf("%d\n", find(2));

    uni(1, 2);
    printf("%d\n", find(1));
    printf("%d\n", find(2));

    uni(2, 3);
    printf("%d\n", find(3));
    printf("%d %d %d\n", getSize(1), getSize(2), getSize(3));
    return 0;
}