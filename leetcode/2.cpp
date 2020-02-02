#include <stdlib.h>
#include <stdio.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

void print(struct ListNode* a) {
    while (a != NULL) {
        printf("%d\n", a->val);
        a = a->next;
    }
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* start = (struct ListNode*)malloc(sizeof(struct ListNode));
    start->val = 0;
    start->next = NULL;
    struct ListNode* now = start, *prev = start;
    int carry = 0;
    
    while (l1 != NULL && l2 != NULL) {
        int val = l1->val + l2->val + carry;
        if (val >= 10) {
            carry = 1;
            val -= 10;
        }
        else {
            carry = 0;
        }
        now->val = val;
        now->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        // move
        l1 = l1->next;
        l2 = l2->next;
        prev = now;
        now = now->next;
    }
    // same length
    if (l1 == NULL && l2 == NULL) {
        if (carry == 1) {
            now->val = 1;
            now->next = NULL;
        }
        else {
            prev->next = NULL;
        }
        return start;
    }
    // make l1 the longer one
    if (l1 == NULL) l1 = l2;
    // add the rest
    while (carry == 1) {
        if (l1 == NULL) {
            now->val = 1;
            now->next = NULL;
            return start;
        }
        int val = l1->val + carry;
        if (val >= 10) {
            carry = 1;
            val -= 10;
        }
        else {
            carry = 0;
        }
        now->val = val;
        now->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        // move
        l1 = l1->next;
        prev = now;
        now = now->next;
    }
    prev->next = l1;
    return start;
}

int main(void) {

    struct ListNode a, b, c;
    a.val = 1;
    a.next = NULL;
    b.val = 9;
    b.next = &c;
    c.val = 9;
    c.next = NULL;
    print(addTwoNumbers(&a, &b));
    return 0;
}

