#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node *next;
} Node;

Node *new(int val) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->val = val;
    node->next = NULL;
    return node;
}
Node *createLinkedList(int* arr, int len) {
    Node* head = new(arr[0]);
    Node* now = head;
    for (int i = 1; i < len; i++) {
        now->next = new(arr[i]);
        now = now->next;
    }
    return head;
}
void print(Node *head) {
    printf("list: ");
    while (head != NULL) {
        printf("%d ", head->val);
        head = head->next;
    }
    puts("");
}
Node *sort(Node *head, int len) {
    if (len == 1) {
        head->next = NULL;
        return head;
    }
    Node *rightHead = head;
    for (int i = 0; i < len / 2; i++) {
        rightHead = rightHead->next;
    }
    Node *left = sort(head, len / 2);
    Node *right = sort(rightHead, len - len / 2);
    // merge: insert right to left
    Node *lNow = left, *rNow = right;
    Node *newHead = new(-1);
    Node *now = newHead;
    while (lNow != NULL && rNow != NULL) {
        if (lNow->val < rNow->val) {
            now->next = lNow;
            now = lNow;
            lNow = lNow->next;
        } else {
            now->next = rNow;
            now = rNow;
            rNow = rNow->next;
        }
    }
    if (lNow == NULL) {
        now->next = rNow;
    } else if (rNow == NULL) {
        now->next = lNow;
    }
    return newHead->next;
}
int main(void) {
    int arr[] = {2, 1, 4, 7, 4, 8, 3, 6, 4, 7};
    Node* head = createLinkedList(arr, 10);
    print(head);
    head = sort(head, 10);
    print(head);
    return 0;
}