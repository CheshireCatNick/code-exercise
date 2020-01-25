#include <stdio.h>
#include <string.h>

#define M 1000010
#define N 50
#define ALPH 26
char lStr[M];
char keyword[N + 10];

typedef struct node {
    node* children[ALPH];
} Node;

void printTrie(Node* root) {
    for (int i = 0; i < ALPH; i++) {
        if (root->children[i] != NULL) {
            printf("%c", 'a' + i);
            printTrie(root->children[i]); 
        }
    }
}

Node* newNode() {
    Node* node = new Node();
    for (int i = 0; i < ALPH; i++) {
        node->children[i] = NULL;
    }
    return node;
}
int main(void) {
    int t, q;
    scanf("%d", &t);
    while (t--) {
        scanf("%s", lStr);
        int l = strlen(lStr);
        Node* str = newNode();
        Node* parent = str;
        for (int i = 0; i < l; i++) {
            parent->children[lStr[i] - 'a'] = newNode();
            parent = parent->children[lStr[i] - 'a'];
        }
        Node* root = newNode();
        Node* strJ, *child;
        for (int i = 0; i < l; i++) {
            parent = root;
            str = str->children[lStr[i] - 'a'];
            strJ = str;
            for (int j = 0; j < N; j++) {
                int cur = i + j;
                if (cur >= l) break;
                char c = lStr[cur] - 'a';
                if (parent->children[c] == NULL) {
                    //printf("%d\n", cur);
                    parent->children[c] = strJ;
                    break;
                    //parent = parent->children[c];
                }
                else {
                    parent = parent->children[c];
                    if (cur + 1 >= l) strJ = NULL;
                    else strJ = strJ->children[lStr[cur + 1] - 'a'];
                    //printf("%c %c\n", c, d);
                }
            }
        }
        //printTrie(root);
        scanf("%d", &q);
        while (q--) {
            scanf("%s", keyword);
            parent = root;
            bool isSubstring = true;
            int l = strlen(keyword);
            for (int i = 0; i < l; i++) {
                if (parent->children[keyword[i] - 'a'] == NULL) {
                    isSubstring = false;
                    break;
                }
                else {
                    parent = parent->children[keyword[i] - 'a'];
                }
            }
            if (isSubstring) puts("y");
            else puts("n");
        }
    }
}